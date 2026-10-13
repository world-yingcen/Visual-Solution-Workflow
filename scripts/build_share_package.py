#!/usr/bin/env python3
"""Build a portable Skill package with explicitly listed tutorial examples.

兩種用法：
- 預設：在 dist/ 建立日期版資料夾與 zip（給沒有 git 的人）。
- --sync DIR：把同一份內容同步到「只放 Skill 的 repo」工作目錄（同事 clone 的那個），
  可加 --commit 訊息與 --push 直接推上去。

來源固定是維護 repo 的 skill/；01_產品/ 等不在清單內的東西不會被帶出去。
"""

import argparse
from datetime import date
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'skill'
DIST = ROOT / 'dist'
SKILLS = (
    'visual-solution-immersive-director',
    'gsap-core',
    'gsap-timeline',
    'gsap-scrolltrigger',
    'gsap-performance',
    'gsap-plugins',
    'gsap-utils',
    'gsap-react',
    'gsap-frameworks',
    'eagle',
    'eagle-visual-solution-curator',
)
ROOT_FILES = ('README.md', 'install.py', 'INSTALL.md', 'AGENTS.md', '轉版狀態.md',
              'index.html', 'guide-tools.html', '使用教學.md', '使用教學.html', '快速索引.md', '快速索引.html',
              'css/manual.css', 'js/copy-code.js', 'js/scroll-top.js', '.gitignore')

# 僅附上使用者指定的教學案例與必要素材；不掃描其他案件。
TUTORIAL_FILES = (
    'Ocean-Medi-歐群生醫/動態腳本-Banner層次與動態分鏡-v1.html',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/cis/official-colors.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/cis/official-patterns.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/cis/official-secondary.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/cis/official-type.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/fonts/nunito-sans-bold.ttf',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/fonts/nunito-sans-light.ttf',
    'Ocean-Medi-歐群生醫/素材/02_設計/assets/fonts/nunito-sans-regular.ttf',
    'Ocean-Medi-歐群生醫/素材/02_設計/banner-motion.css',
    'Ocean-Medi-歐群生醫/素材/02_設計/banner-motion.js',
    'Ocean-Medi-歐群生醫/素材/02_設計/cis.css',
    'Ocean-Medi-歐群生醫/素材/02_設計/ocean-core.css',
    'Ocean-Medi-歐群生醫/素材/02_設計/ocean-core.js',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-00-core.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-01-wellness.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-02-environment.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-03-energy.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-contact.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/qa/try02-2560x1280-transition.png',
    'Ocean-Medi-歐群生醫/素材/02_設計/核心視覺片段.html',
    'Ocean-Medi-歐群生醫/素材/修片＿網站照片/DSC00230.webp',
    'Ocean-Medi-歐群生醫/素材/修片＿網站照片/DSC00253.webp',
    'Ocean-Medi-歐群生醫/素材/修片＿網站照片/DSC00272.webp',
    'Ocean-Medi-歐群生醫/素材/修片＿網站照片/DSC00457.webp',
    'Ocean-Medi-歐群生醫/素材/首次設計/01 LOGO_OK/標誌中文置中標準組合(白色logo).png',
    'Ocean-Medi-歐群生醫/素材/首次設計/01 LOGO_OK/標誌中文置中標準組合_標準色logo.png',
    'Ocean-Medi-歐群生醫/視覺提案-v1.html',
    'examples/ocean-medi/motion-end.png',
    'examples/ocean-medi/motion-middle.png',
    'examples/ocean-medi/motion-start.png',
    'examples/ocean-medi/visual-proposal.png',
    'Ichia-毅嘉科技/動態腳本-v1.html',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ems-film.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ems-fpc.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ems-miniled.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ems-pcba.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/esg-forest.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/grid-deco-src.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/grid-light.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ims-console.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ims-hmi-off.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ims-hmi-on.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/ims-stone-on.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/logo.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/map-light.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/site-linkou.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/site-malaysia.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/tms-cfd.webp',
    'Ichia-毅嘉科技/素材/00_整體視覺設計/assets/tms-fin.webp',
    'Ichia-毅嘉科技/視覺提案-v1.html',
    'examples/ichia/motion-end.png',
    'examples/ichia/motion-middle.png',
    'examples/ichia/motion-start.png',
    'examples/ichia/visual-proposal.png',
)
IGNORE = shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc')


def copy_package(target):
    """把 skill/ 內明列的根目錄檔案、11 支 Skill 與 tests 放進 target；skills/ 與 tests/ 整個重建。"""
    for filename in ROOT_FILES + TUTORIAL_FILES:
        source = PACKAGE / filename
        if not source.is_file():
            raise SystemExit('缺少檔案：skill/%s' % filename)
        (target / filename).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target / filename)
    skills_dir = target / 'skills'
    if skills_dir.exists():
        shutil.rmtree(skills_dir)
    for skill in SKILLS:
        source = PACKAGE / 'skills' / skill
        if not (source / 'SKILL.md').is_file():
            raise SystemExit('缺少 Skill：%s' % skill)
        shutil.copytree(source, skills_dir / skill, ignore=IGNORE)
    tests = target / 'tests'
    if tests.exists():
        shutil.rmtree(tests)
    shutil.copytree(PACKAGE / 'tests', tests, ignore=IGNORE)


def build(stamp):
    name = 'visual-solution-skills-%s' % stamp
    target = DIST / name
    archive = DIST / (name + '.zip')
    if target.exists() or archive.exists():
        raise SystemExit('輸出已存在，未覆蓋：%s' % name)
    target.mkdir(parents=True)
    copy_package(target)
    shutil.make_archive(str(archive.with_suffix('')), 'zip', DIST, name)
    return target, archive


def git(target, *args):
    done = subprocess.run(('git', '-C', str(target)) + args, capture_output=True, text=True)
    return done.returncode == 0, (done.stdout + done.stderr).strip()


def sync(target, commit=None, push=False):
    """同步到只放 Skill 的 repo 工作目錄；可選擇直接 commit 與 push。"""
    target = Path(target).expanduser().resolve()
    if not (target / '.git').exists():
        raise SystemExit('目標不是 git 工作目錄：%s（先 git clone 那個 repo，或 git init）' % target)
    if target in (ROOT, PACKAGE):
        raise SystemExit('目標不能是維護 repo 或它的 skill/ 本身')
    copy_package(target)
    ok, status = git(target, 'status', '--short')
    lines = ['已同步到：%s' % target]
    if not status:
        lines.append('內容與上次相同，沒有東西要提交。')
        return lines
    lines += ['變更：'] + ['  ' + line for line in status.splitlines()[:40]]
    if commit is None:
        lines.append('尚未提交；加 --commit "訊息" 提交，--push 推送。')
        return lines
    git(target, 'add', '-A')
    ok, out = git(target, 'commit', '-m', commit)
    lines.append(out.splitlines()[0] if out else '已提交')
    if not ok:
        return lines
    if push:
        ok, out = git(target, 'push')
        lines.append(out if ok else '推送失敗：%s' % out)
    else:
        lines.append('尚未推送；加 --push 推上去。')
    return lines


def main():
    parser = argparse.ArgumentParser(description='從 skill/ 建立可分享的 Skill 套件，或同步到只放 Skill 的 repo')
    parser.add_argument('--date', default=date.today().strftime('%Y%m%d'),
                        help='dist 輸出日期，格式 YYYYMMDD')
    parser.add_argument('--sync', metavar='DIR', help='同步到這個 git 工作目錄（同事 clone 的 Skill repo）')
    parser.add_argument('--commit', metavar='訊息', help='同步後直接 commit（需搭配 --sync）')
    parser.add_argument('--push', action='store_true', help='commit 後推送到 origin（需搭配 --commit）')
    args = parser.parse_args()
    if args.push and not args.commit:
        raise SystemExit('--push 需要搭配 --commit')
    if args.commit and not args.sync:
        raise SystemExit('--commit 需要搭配 --sync')
    if args.sync:
        print('\n'.join(sync(args.sync, args.commit, args.push)))
        return
    if len(args.date) != 8 or not args.date.isdigit():
        raise SystemExit('--date 必須是 YYYYMMDD')
    target, archive = build(args.date)
    print(target)
    print(archive)


if __name__ == '__main__':
    main()
