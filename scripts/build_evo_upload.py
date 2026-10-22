#!/usr/bin/env python3
"""Package the paired Lin/Miffy sources and the unchanged engineer HTML kit."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile
from zoneinfo import ZoneInfo

NAME = 'lin-evo-miffy-evo'
IGNORE = shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc', '.git',
                                'node_modules', 'agents')


def resolve_sources(source=None, lin_source=None, miffy_source=None):
    configured = {}
    if source is not None:
        source = source.expanduser().resolve()
        config = source / 'skill-sources.json'
        if config.is_file():
            configured = json.loads(config.read_text())
    result = {}
    for name, override in (('Lin-EVO', lin_source), ('Miffy-EVO', miffy_source)):
        if override is not None:
            path = override.expanduser().resolve()
        elif source is not None:
            path = (source / configured.get(name, name)).resolve()
        else:
            raise ValueError('請提供 --source，或同時提供 --lin-source 與 --miffy-source。')
        if not (path / 'SKILL.md').is_file() or not (path / 'references').is_dir():
            raise ValueError(f'{name} 來源不完整：{path}')
        result[name] = path
    return result


def source_record(path):
    record = {'path': str(path), 'git_root': None, 'commit': None,
              'working_tree_modified': None}
    # Do not attribute an untracked external skill to an unrelated parent repo.
    try:
        repo = Path(subprocess.check_output(
            ['git', '-C', str(path), 'rev-parse', '--show-toplevel'],
            text=True, stderr=subprocess.DEVNULL).strip()).resolve()
        relative = (path / 'SKILL.md').relative_to(repo).as_posix()
        subprocess.check_output(['git', '-C', str(repo), 'ls-files',
                                 '--error-unmatch', '--', relative],
                                stderr=subprocess.DEVNULL)
        record.update({
            'git_root': str(repo),
            'commit': subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip(),
            'working_tree_modified': bool(subprocess.check_output(
                ['git', '-C', str(path), 'status', '--porcelain', '--', '.'], text=True).strip()),
        })
    except (subprocess.CalledProcessError, OSError, ValueError):
        pass
    record['files'] = {
        p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(path.rglob('*')) if p.is_file()
        and not any(part in ('.DS_Store', '__pycache__', '.git', 'node_modules', 'agents')
                    for part in p.relative_to(path).parts) and p.suffix != '.pyc'
    }
    return record


def build(source, output, lin_source=None, miffy_source=None):
    if output.exists():
        raise ValueError(f'輸出已存在，不覆蓋：{output}')
    sources = resolve_sources(source, lin_source, miffy_source)
    kit = sources['Miffy-EVO'] / 'evomni-html'
    for name in ('VERSION', 'SKILL.md', 'references/spec.md',
                 'references/checklist.md', 'scripts/check-site.mjs',
                 'example-site/index.html'):
        if not (kit / name).is_file():
            raise ValueError(f'缺少工程師套件檔案：{name}')
    provenance = {name: source_record(path) for name, path in sources.items()}
    with tempfile.TemporaryDirectory() as temp:
        package = Path(temp) / NAME
        for name in ('Lin-EVO', 'Miffy-EVO'):
            target = package / 'resources' / name
            shutil.copytree(sources[name], target, ignore=IGNORE)
            (target / 'SKILL.md').rename(target / 'GUIDE.md')
        # Preserve the engineer kit byte-for-byte; adapt only wrapper links.
        for path in (package / 'resources').rglob('*.md'):
            if 'evomni-html' in path.parts:
                continue
            text = path.read_text()
            for name in ('Lin-EVO', 'Miffy-EVO'):
                text = text.replace(f'{name}/SKILL.md', f'{name}/GUIDE.md')
            path.write_text(text)
        (package / 'SKILL.md').write_text('''---
name: lin-evo-miffy-evo
description: 在 Claude 網頁／App 製作與校稿靜態網站，或將已確認網站轉成 EVO 匯入包；依使用者指定的 Lin-EVO／Miffy-EVO 分流，內附工程師整站 HTML 套件。
---

# Lin-EVO＋Miffy-EVO

此包提供兩個接續工作的入口：使用者說「使用 Lin-EVO」時完整讀取
[Lin-EVO 規範](resources/Lin-EVO/GUIDE.md)；說「使用 Miffy-EVO」時完整讀取
[Miffy-EVO 規範](resources/Miffy-EVO/GUIDE.md)，再讀該流程要求的參考。
這些是本包的工作指南，不需另外安裝。保留已確認的設計、內容與 RWD 範圍。

## 上傳環境的優先規則

- 本包是來源快照，不執行指南中僅適用本機的 install.py、安裝清單查找或 Skill 來源 Git 更新。
  更新本包需由維護者重新打包並由使用者重新上傳；停用舊版 Lin／Miffy，避免重複規範。
- 案件 Git 另行處理：有實際工具時每輪依指南 fetch 並核對版本，缺工具時提供步驟，
  不假稱已同步。尚未轉 EVO 的 Git 切版案件換電腦前，確認範圍後須 commit 並 push 成功，
  另一台取得同一版本並先讀交接。已成功轉 EVO 的案件改至後台，原靜態 Git 不再修改或 push。
- 只讀使用者提供或工具實際可存取的案件檔案；不能假設可讀本機路徑、localhost、
  公司內網或使用者登入的後台。需要完整 HTML、CSS、JS、素材與案件交接紀錄。
- 整站 HTML 工程師套件位於 resources/Miffy-EVO/evomni-html/；Lin 與 Miffy
  都使用同一份。每輪讀 VERSION 與 SKILL.md，依要求讀 spec.md；套件由人工更新，
  不宣稱已自動確認工程師最新版。原始工程師檔案未改寫。
- 新整站先核對目標支援整站 HTML 匯入；既有 JSON 案件沿用 Miffy 的 legacy-workflow.md，
  本包不包含舊 JSON 工具庫，缺工具時列出缺口，不混用兩種包。
- 有程式執行能力才編譯、執行檢查器與打包；有瀏覽器才實看。Node 不可用時，依工程師
  checklist 檢核後交後台預檢，請使用者回傳報告；不手造 evomni-check.json。
- 實際上傳、匯入與發布依使用者指定的站台及授權；缺操作工具時提供可下載成果和手動步驟。
  本機檢查、後台匯入、編輯儲存及發布後前台分開記錄，未執行標待驗。
- 圖片處理沿用本案分工；不因打包而擅自降低畫質。工程師套件、示範網站與本包來源紀錄
  不混進客戶網站交付 ZIP。

兩個 Skill 各自的來源路徑、可用的 Git commit、工程師套件版本與檔案雜湊見 SOURCE.json。打包驗證不代表已在 Claude
上傳執行，也不代表已在本案 EVO 後台完成驗收。
''')
        failures = []
        for path in package.rglob('*.md'):
            if 'evomni-html' in path.parts:
                continue
            for href in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if href.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                target = (path.parent / href.split('#')[0]).resolve()
                if not target.is_relative_to(package.resolve()) or not target.exists():
                    failures.append(f'{path.relative_to(package)} -> {href}')
        if failures:
            raise ValueError('參考連結缺漏：\n' + '\n'.join(failures))
        for path in kit.rglob('*'):
            if path.is_file() and not any(part in ('.DS_Store', '__pycache__', '.git', 'node_modules', 'agents') for part in path.parts) and path.suffix != '.pyc':
                copied = package / 'resources/Miffy-EVO/evomni-html' / path.relative_to(kit)
                if path.read_bytes() != copied.read_bytes():
                    raise ValueError(f'工程師套件內容不一致：{path}')
        hashes = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(package.rglob('*')) if p.is_file()}
        (package / 'SOURCE.json').write_text(json.dumps({
            'built_at': datetime.now(ZoneInfo('Asia/Taipei')).isoformat(),
            'sources': provenance,
            'engineer_kit_version': (kit / 'VERSION').read_text().strip(),
            'files': hashes,
        }, ensure_ascii=False, indent=2) + '\n')
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob('*')):
                if path.is_file():
                    archive.write(path, path.relative_to(package.parent))
        with zipfile.ZipFile(output) as archive:
            if archive.testzip() is not None:
                raise ValueError('ZIP 完整性檢查失敗')
        print(f'已建立並核對：{output}（{output.stat().st_size:,} bytes；工程師套件 {(kit / "VERSION").read_text().strip()}）')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='來源管理資料夾；有 skill-sources.json 時依設定定位兩個 Skill')
    parser.add_argument('--lin-source', type=Path, help='Lin-EVO 資料夾，可覆寫 --source 的設定')
    parser.add_argument('--miffy-source', type=Path, help='Miffy-EVO 資料夾，可覆寫 --source 的設定')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        build(args.source, args.output.expanduser().resolve(), args.lin_source, args.miffy_source)
    except (ValueError, OSError) as error:
        parser.exit(1, f'打包未完成：{error}\n')
