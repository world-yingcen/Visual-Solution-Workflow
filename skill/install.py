#!/usr/bin/env python3
"""Install the visual-solution workflow skills into a skills directory.

Only touches entries this installer created (tracked in a manifest); never
removes or overwrites an unrelated skill folder.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

MANIFEST = '.visual-solution-install.json'
IGNORE = shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc', '.git')

# 現行流程只有一個主入口；GSAP_SUPPORT 是主 Skill 可按需讀取的技術支援，
# EAGLE 是團隊共用的資源庫工具。它們都隨分享包安裝，但不是額外製作角色。
PRIMARY = (
    'visual-solution-immersive-director',
)
GSAP_SUPPORT = (
    'gsap-core',
    'gsap-timeline',
    'gsap-scrolltrigger',
    'gsap-performance',
    'gsap-plugins',
    'gsap-utils',
    'gsap-react',
    'gsap-frameworks',
)
EAGLE = (
    'eagle',
    'eagle-visual-solution-curator',
)
REQUIRED = PRIMARY + GSAP_SUPPORT + EAGLE
LEGACY = {'visual-solution-workflow', 'visual-solution-project-prd',
          'visual-solution-brand-analysis', 'visual-solution-visual-director',
          'visual-solution-page-builder', 'visual-solution-requirements-review'}


# 案件資料夾的權限預設。Claude Code 不會往上層找設定，每個案件根目錄都要自己有一份。
CASE_SETTINGS = {
    'permissions': {
        'defaultMode': 'acceptEdits',
        # 切版要開瀏覽器看預覽、截圖比對，這些都不在檔案工具裡。
        'allow': [
            'Bash', 'Edit', 'Write', 'WebFetch',
            'mcp__Claude_in_Chrome__navigate',
            'mcp__Claude_in_Chrome__read_page',
            'mcp__Claude_in_Chrome__get_page_text',
            'mcp__Claude_in_Chrome__read_console_messages',
            'mcp__Claude_in_Chrome__read_network_requests',
            'mcp__Claude_in_Chrome__computer',
            'mcp__Claude_in_Chrome__find',
            'mcp__Claude_in_Chrome__resize_window',
            'mcp__Claude_in_Chrome__tabs_create_mcp',
            'mcp__Claude_in_Chrome__tabs_close_mcp',
            'mcp__computer-use__screenshot',
            'mcp__computer-use__left_click',
            'mcp__computer-use__key',
            'mcp__computer-use__type',
            'mcp__computer-use__scroll',
            'mcp__computer-use__open_application',
        ],
        'deny': [
            'Bash(git push --force*)',
            'Bash(git push -f *)',
            'Bash(git reset --hard*)',
            'Bash(rm -rf /*)',
            'Bash(rm -rf ~*)',
        ],
    }
}


def default_target():
    return Path.home() / '.claude' / 'skills'


def setup_case(case, dry_run=False):
    """Write the permission defaults into a client case folder."""
    lines = ['案件資料夾：%s' % case]
    if not case.is_dir():
        lines.append('中止：找不到這個資料夾。請給案件根目錄的完整路徑。')
        return 1, lines
    path = case / '.claude' / 'settings.json'
    if path.is_file():
        lines.append('[跳過] 已有 .claude/settings.json，未覆蓋。要換成預設值請先自行備份或刪除。')
        return 0, lines
    lines.append('[新增] .claude/settings.json（切版、檔案修改與指令不再逐項詢問；'
                 '強制推送、reset --hard 與 rm -rf 仍擋下）')
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(CASE_SETTINGS, ensure_ascii=False, indent=2) + '\n',
                        encoding='utf-8')
    lines.append('')
    lines.append('完成%s。案件子資料夾（06-切版 等）會沿用同一份設定。'
                 % ('（試跑，未實際寫入）' if dry_run else ''))
    lines.append('注意：流程規定要專案人員確認的節點不受影響，仍要人工確認。')
    return 0, lines


def sources(root):
    """Return only the explicitly supported bundle."""
    base = root / 'skills'
    if not base.is_dir():
        return {}
    found = {}
    for name in REQUIRED:
        path = base / name
        if path.is_dir() and (path / 'SKILL.md').is_file():
            found[name] = path
    return found


def declared_name(folder):
    """The name: value in SKILL.md front matter, or None when absent."""
    head = folder.joinpath('SKILL.md').read_text(encoding='utf-8', errors='replace')[:2000]
    match = re.search(r'^name:\s*(\S+)\s*$', head, re.MULTILINE)
    return match.group(1) if match else None


def read_manifest(target):
    path = target / MANIFEST
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def owned(target):
    """Names this installer previously installed into target."""
    names = read_manifest(target).get('skills')
    return set(names) if isinstance(names, list) else set()


def supports_symlink(target):
    """Windows only allows symlinks with developer mode or admin rights."""
    while not target.is_dir() and target.parent != target:
        target = target.parent
    probe = Path(tempfile.mkdtemp(dir=str(target)))
    try:
        link = probe / 'probe'
        os.symlink(str(probe), str(link), target_is_directory=True)
        return True
    except (OSError, NotImplementedError, AttributeError):
        return False
    finally:
        shutil.rmtree(probe, ignore_errors=True)


def remove(path):
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def install(root, target, mode='auto', dry_run=False):
    """Link or copy the complete supported bundle."""
    lines = []
    found = sources(root)
    missing = [n for n in REQUIRED if n not in found]
    if missing:
        lines.append('中止：來源缺少必要 Skill %s' % '、'.join(missing))
        lines.append('請確認分享包完整；主 Skill、8 個 GSAP 技術支援及本次選用工具都必須存在。')
        return 1, lines

    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)
    elif not target.is_dir():
        lines.append('（試跑）安裝位置尚未建立，實際執行時會自動建立：%s' % target)

    if mode == 'auto':
        mode = 'symlink' if supports_symlink(target) else 'copy'
    lines.append('安裝位置：%s' % target)
    lines.append('安裝方式：%s' % ('捷徑（改 repo 就直接生效）' if mode == 'symlink'
                                   else '複製（repo 更新後要重跑這支腳本）'))
    lines.append('安裝內容：主 Skill＋8 個 GSAP 技術支援＋2 個 Eagle 資源庫工具')
    lines.append('')

    mine = owned(target)
    installed, blocked = [], []
    for name, src in found.items():
        dst = target / name
        stated = declared_name(src)
        if stated and stated != name:
            lines.append('[提醒] %s：SKILL.md 寫的是 name: %s，與資料夾名不一致，可能無法載入'
                         % (name, stated))
        if dst.exists() and not dst.is_symlink() and name not in mine:
            blocked.append(name)
            lines.append('[跳過] %s：該位置已有其他來源的資料夾，未動它' % name)
            continue
        action = '更新' if dst.exists() or dst.is_symlink() else '新增'
        installed.append(name)
        lines.append('[%s] %s' % (action, name))
        if dry_run:
            continue
        remove(dst)
        if mode == 'symlink':
            os.symlink(str(src), str(dst), target_is_directory=True)
        else:
            shutil.copytree(str(src), str(dst), ignore=IGNORE)

    if not dry_run and installed:
        (target / MANIFEST).write_text(json.dumps(
            dict(source=str(root), mode=mode, skills=sorted(set(mine) | set(installed))),
            ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines.append('')
    if blocked:
        lines.append('未完成：%d 支被跳過。請人工確認上列資料夾要保留還是換掉，'
                     '確認後把它移走再重跑。' % len(blocked))
        return 1, lines
    lines.append('完成：%d 支已安裝%s。' % (len(installed), '（試跑，未實際寫入）' if dry_run else ''))
    lines.append('下一步：重新載入對應的 AI 工具，技能清單就會出現這些 Skill。')
    return 0, lines


def status(target):
    lines = ['安裝位置：%s' % target]
    manifest = read_manifest(target)
    if manifest.get('source'):
        lines.append('來源 repo：%s' % manifest['source'])
        lines.append('安裝方式：%s' % ('捷徑' if manifest.get('mode') == 'symlink' else '複製'))
    lines.append('')
    ok = True
    extra = sorted(owned(target) - set(REQUIRED))
    for name in list(REQUIRED) + extra:
        if name in LEGACY:
            lines.append('[歷史殘留] %s：已停用，未自動移除；現行請用主 Skill。' % name)
            continue
        path = target / name
        if path.is_symlink():
            resolved = path.resolve()
            good = (resolved / 'SKILL.md').is_file()
            ok = ok and good
            lines.append('[%s] %s（捷徑 → %s）' % ('正常' if good else '斷掉', name, resolved))
        elif (path / 'SKILL.md').is_file():
            lines.append('[正常] %s（複製）' % name)
        else:
            ok = False
            lines.append('[未安裝] %s' % name)
    lines.append('')
    if ok:
        lines.append('主 Skill 正常，可以使用。%s'
                     % ('另有選配 %s。' % '、'.join(extra) if extra else ''))
    else:
        lines.append('有項目缺少或捷徑失效，請核對安裝來源。')
    return 0 if ok else 1, lines


def git(root, *args, timeout=120):
    """在套件資料夾跑 git；回傳 (成功, 輸出)。git 不在或逾時都算失敗，不丟例外。"""
    try:
        done = subprocess.run(('git', '-C', str(root)) + args, capture_output=True,
                              text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as err:
        return False, str(err)
    out = (done.stdout + done.stderr).strip()
    return done.returncode == 0, out


def update(root, target, dry_run=False):
    """取得新版套件內容：git pull，複製安裝再同步一次到安裝位置。"""
    lines = ['套件位置：%s' % root]
    # 套件可能是 repo 的子資料夾（例如 Visual-Solution-Workflow/skill），所以用 git 找 repo，不看 root/.git
    inside_repo, _ = git(root, 'rev-parse', '--show-toplevel')
    if not inside_repo:
        lines += ['', '這個資料夾不是 git clone，沒辦法自動更新。',
                  '向維護者取得新版資料夾覆蓋這一份，若當初是複製安裝，覆蓋後再跑一次 install.py。']
        return 1, lines

    ok, head_before = git(root, 'rev-parse', 'HEAD')
    if not ok:
        lines += ['', '讀不到目前版本：%s' % head_before]
        return 1, lines
    mode = read_manifest(target).get('mode')
    lines.append('目前版本：%s' % head_before[:8])
    if dry_run:
        lines += ['', '試跑：會執行 git pull --ff-only，不實際更新。']
        return 0, lines

    ok, out = git(root, 'pull', '--ff-only')
    if not ok:
        lines += ['', '更新失敗（未同步技能檔案）：', out, '']
        if 'FETCH_HEAD' in out and 'Operation not permitted' in out:
            lines += ['目前執行環境無法寫入來源庫的 Git 暫存檔；這不代表遠端 repo 拒絕存取。',
                      '確認來源庫狀態與 --target 後，取得執行環境的寫入核准，再重跑同一命令。',
                      '不要為此修改檔案權限或重置 Git 歷史。']
        else:
            lines += ['常見原因：沒有網路、沒有這個 repo 的權限，或本機有未推送的修改造成分歧。',
                      '維護者自己的電腦有未推送的 commit 屬正常，不必更新。']
        return 1, lines

    ok, head_after = git(root, 'rev-parse', 'HEAD')
    if ok and head_after == head_before:
        lines += ['', '已經是最新版，沒有東西要更新。']
        return 0, lines

    lines.append('更新後版本：%s' % head_after[:8])
    ok, log = git(root, 'log', '--oneline', '%s..%s' % (head_before, head_after))
    if ok and log:
        lines += ['', '這次拿到的更新：'] + ['  ' + line for line in log.splitlines()[:20]]
    lines.append('')
    if mode == 'copy':
        code, sync = install(root, target, 'copy', dry_run=False)
        lines += ['複製安裝，已同步到安裝位置：', ''] + sync
        return code, lines
    lines.append('捷徑安裝，新版內容已直接生效；重新載入對應的 AI 工具即可使用。')
    return 0, lines


def uninstall(target, dry_run=False):
    lines = ['安裝位置：%s' % target, '']
    mine = owned(target)
    removed = []
    for name in sorted(mine):
        path = target / name
        if not path.exists() and not path.is_symlink():
            lines.append('[已不存在] %s' % name)
            continue
        removed.append(name)
        lines.append('[移除] %s' % name)
        if not dry_run:
            remove(path)
    if not dry_run:
        manifest = target / MANIFEST
        if manifest.is_file():
            manifest.unlink()
    lines.append('')
    if not mine:
        lines.append('沒有本腳本安裝的紀錄，未移除任何東西。')
    else:
        lines.append('已移除 %d 支%s。repo 本身不受影響。'
                     % (len(removed), '（試跑，未實際移除）' if dry_run else ''))
    return 0, lines


def main():
    parser = argparse.ArgumentParser(description='安裝整體視覺主 Skill 與 GSAP 技術支援')
    parser.add_argument('--target', help='安裝位置，預設 ~/.claude/skills')
    parser.add_argument('--copy', action='store_true', help='強制用複製，不建捷徑')
    parser.add_argument('--dry-run', action='store_true', help='只顯示會做什麼，不實際寫入')
    parser.add_argument('--status', action='store_true', help='檢查目前安裝狀態')
    parser.add_argument('--update', action='store_true', help='取得新版套件內容（git pull），複製安裝會一併同步')
    parser.add_argument('--uninstall', action='store_true', help='移除本腳本安裝的項目')
    parser.add_argument('--case', help='在指定案件資料夾建立 .claude/settings.json，製作時不再逐項詢問')
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    target = Path(args.target).expanduser().resolve() if args.target else default_target()
    if args.case:
        code, lines = setup_case(Path(args.case).expanduser().resolve(), args.dry_run)
    elif args.status:
        code, lines = status(target)
    elif args.update:
        code, lines = update(root, target, args.dry_run)
    elif args.uninstall:
        code, lines = uninstall(target, args.dry_run)
    else:
        code, lines = install(root, target, 'copy' if args.copy else 'auto',
                              args.dry_run)
    print('\n'.join(lines))
    return code


if __name__ == '__main__':
    sys.exit(main())
