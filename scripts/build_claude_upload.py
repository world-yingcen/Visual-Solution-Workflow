#!/usr/bin/env python3
"""Build one self-contained Claude web/App Skill, without local installers."""
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

ROOT = Path(__file__).resolve().parents[1]
NAME = 'visual-solution-cloud'
SUPPORT = ('gsap-core', 'gsap-timeline', 'gsap-scrolltrigger', 'gsap-performance',
           'gsap-plugins', 'gsap-utils', 'gsap-react', 'gsap-frameworks',
           'eagle', 'eagle-visual-solution-curator')
IGNORE = shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc', '.git', 'agents')


def revision(path):
    result = subprocess.run(['git', '-C', str(path), 'rev-parse', 'HEAD'],
                            capture_output=True, text=True, check=True)
    dirty = subprocess.run(['git', '-C', str(path), 'status', '--porcelain'],
                           capture_output=True, text=True, check=True).stdout
    return {'commit': result.stdout.strip(), 'working_tree_modified': bool(dirty)}


def between(text, start, end, replacement):
    a, b = text.index(start), text.index(end, text.index(start))
    return text[:a] + replacement + '\n\n' + text[b:]


def copy_guide(source, target):
    if not (source / 'SKILL.md').is_file():
        raise ValueError('缺少來源 Skill：' + str(source))
    shutil.copytree(source, target, ignore=IGNORE)
    (target / 'SKILL.md').rename(target / 'GUIDE.md')


def prepare(package, lin):
    resources = package / 'resources'
    workflow = resources / 'workflow'
    copy_guide(ROOT / 'skill/skills/visual-solution-immersive-director', workflow)
    copy_guide(lin, resources / 'lin')
    for name in SUPPORT:
        copy_guide(ROOT / 'skill/skills' / name, resources / name)

    p = workflow / 'GUIDE.md'
    text = p.read_text()
    text = between(text, '每次開始新一輪工作', '遇到 PDF 時',
                   '此為 Claude 網頁／App 上傳快照。每輪先重讀本包規範與已提供的案件進度；'
                   '不執行本機 install.py、Plugin 安裝或套件來源 Git 更新。'
                   '原始來源維護仍用 Git，更新上傳版須重新打包並上傳。')
    text = text.replace('使用本執行端的 lin-frontend 更新並重讀共用規範',
                        '讀取本包 resources/lin/GUIDE.md 與本輪對應參考')
    text = between(text, '## 建議分工', '## 確認與持續推進',
                   '## 網頁／App 執行分工\n\n'
                   '由目前 Claude 依可用工具完成已授權工作。產圖先整理素材工單；'
                   '有本次可用且已授權的產圖工具才使用，否則交付 prompt，'
                   '請使用者產圖後提供成品。不預设可操作本機 Chrome、ChatGPT 登入分頁或 Codex。'
                   '需要本機切版／瀏覽器實測而此環境不可執行時，產出程式與交接說明，'
                   '標記未驗證；不要求沒有接入的跨工具派工授權。'
                   '圖片壓縮／转檔仍由使用者自行處理，Claude 不代做。')
    p.write_text(text.replace('預设', '預設').replace('转檔', '轉檔'))

    p = resources / 'lin/GUIDE.md'
    text = p.read_text()
    text = between(text, '## 每輪工作：', '先讀案件說明、',
                   '## 上傳包的工作環境\n\n'
                   '本包已內附 LIN 快照。每輪重讀此文件及必要 references，不安裝獨立 Skill、'
                   '不執行 install.py 或對上傳包 git pull。只使用已提供的案件檔案與實際可用工具；'
                   '不假設能讀使用者電腦或公司內網。正式平台契約仍要核對，缺資料列待確認。\n\n'
                   '## 開始工作\n\n')
    p.write_text(text)

    (workflow / 'references/frontend-standards.md').write_text(
        '# 共用切版規範｜本包 LIN 快照\n\n'
        '切版／修改／校稿前必讀 [LIN 工作規則](../../lin/GUIDE.md)，'
        '再按需讀 ../../lin/references/ 的對應規範。本包只作可攜式來源快照，'
        '不要求另行安裝或存取本機 Git；線上來源更新不會自動更新此上傳包。\n\n'
        '品牌方向、確認關卡與 2560×1280 桌機優先仍依 workflow。'
        'LIN 提供共用工程規範；缺平台資料或正式環境時記錄未驗證，'
        '不能把靜態預覽當成後台編輯／發布驗證通過。\n')

    p = workflow / 'references/asset-production.md'
    text = p.read_text()
    lines = text.splitlines()
    lines = [('- 生成素材：先寫本案素材工單與 prompt，使用本次實際可用且已授權的影像工具。'
              '工具不可用時交付 prompt，請使用者產圖後提供成品；不假設能操作本機 Chrome '
              '或已登入的 ChatGPT。保留來源與確認狀態，正式 Logo／產品／IP 使用客供原檔。')
             if line.startswith('- 生成素材：') else line for line in lines]
    p.write_text('\n'.join(lines) + '\n')

    p = workflow / 'references/gsap-skills.md'
    text = p.read_text().replace('請使用根目錄安裝程式安裝整包，不只單獨搬主 Skill。',
                                 '本上傳包已內附為 resources 下的 GUIDE.md，按需讀取，不另行安裝。')
    p.write_text(text)

    # Embedded guides are resources, not additional independently installed Skills.
    for p in package.rglob('*.md'):
        text = p.read_text()
        text = text.replace('../visual-solution-immersive-director/', '../workflow/')
        text = re.sub(r'(\]\([^\n)]*/)(SKILL\.md)([)#])', r'\1GUIDE.md\3', text)
        # Repair inherited references/foo.md links only when foo exists beside the guide.
        def repair(match):
            label, href = match.group(1), match.group(2)
            if href.startswith('references/') and not (p.parent / href.split('#')[0]).exists():
                short = href[len('references/'):]
                if (p.parent / short.split('#')[0]).exists():
                    return f'[{label}]({short})'
            return match.group(0)
        text = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', repair, text)
        text = re.sub(r'/Users/[^\s`<>"\)]+', '（本案提供的工具／案件路徑）', text)
        p.write_text(text)

    (package / 'SKILL.md').write_text('''---
name: visual-solution-cloud
description: 在 Claude 網頁／App 依品牌資料規劃與製作整體視覺網站，內附 LIN 切版、SEO、系統搜尋／詢問車、GSAP 與工程師交接規範；適用提案、切版、校稿與續作。
---

# 整體視覺網站｜Claude 網頁／App 上傳版

以繁體中文與台灣用語協作。先讀 [整體視覺主流程](resources/workflow/GUIDE.md)，
切版／修改／校稿再讀 [LIN](resources/lin/GUIDE.md)，只載入當前需要的參考。
resources 內的 GUIDE.md 都是本包參考，不是需要另外安裝的 Skill。

## 此上傳環境的優先規則

本節優先於參考中僅適用本機的安裝、更新、工具或派工指令；
品牌、設計、工程與使用者已確認規格仍保留，不擅自降低交付要求。

- 這是來源版本快照，不能自動連到使用者本機 Git 或追蹤 GitHub 最新版。
  每輪重讀本包與案件進度；更新規則需由維護者重新打包、由使用者重新上傳。
  不執行 install.py、Plugin 安裝、本機清理或外部部署。
- 只讀對話已提供或工具已授權可存取的檔案。不能直接讀使用者的 /Users 路徑、
  Google Drive 同步資料夾、公司內網或 localhost。需要來源時請使用者提供相關
  HTML／CSS／JS、文字或重點截圖；連結能否存取以本次工具結果為準。
- 本包內附系統參考已核對的規則與搜尋 CSS，但沒有本案後台、
  evomni-page-composer 工程工具庫或客戶素材；不能編造平台 API／資料綁定。
- Chrome、Eagle、Codex 派工與影像工具只在本次確實可用並已授權時操作。
  不可用時完成不依賴工具的部分並列缺口，不要求先安裝全部工具才開始。
- 有程式執行能力才處理已提供的工程；有瀏覽器才實看、實測。
  缺能力時提供可下載成果與驗收步驟，明列未驗證，不宣稱已測通過。
  預設第一階段 2560×1280 桌機，RWD 待使用者另行要求。
- 單一 PDF 超過 10 MB 一律不讀，請提供重點截圖或 .md；未超過上限先問
  現在讀或用到再讀。圖片容量與格式要檢查，轉檔／壓縮由使用者自行處理。
- 每頁只有一個 h1 是公司內部規定；其餘 SEO 責任依 LIN。
  搜尋結果區沿用完整系統 HTML／CSS；詢問車是不可改的公版功能。
  動態須有一般／減少動態兩模式，GSAP pin／scrub 不可留下隱藏內容或留白。
- 切版完成後建立或更新唯一的「工程師交接說明.md」，
  記錄資源、功能、可編輯需求、待接入與兩模式驗收狀態。
  保留方向／視覺／動態／核心片段／整頁確認關卡。

## 主要工程參考

- [HTML／SCSS](resources/lin/references/html-css-rules.md)
- [JavaScript](resources/lin/references/javascript-rules.md)
- [切版端 SEO](resources/lin/references/frontend-seo.md)
- [系統搜尋頁](resources/lin/references/evo-search-reference.md)
- [公版詢問車](resources/lin/references/evo-inquiry-cart-reference.md)
- [EVO 套件宣告](resources/lin/references/evo-vendor-libraries.md)
- [雙模式動態](resources/lin/references/reduced-motion.md)
- [工程師交接](resources/lin/references/engineer-handoff.md)
- [GSAP 按需索引](resources/workflow/references/gsap-skills.md)

來源 commit 與內容雜湊見 SOURCE.json。上傳後仍需在 Claude 啟用並測試。
''')


def validate(package):
    if list(package.rglob('SKILL.md')) != [package / 'SKILL.md']:
        raise ValueError('上傳包必須只有一份入口 SKILL.md')
    failures = []
    for p in package.rglob('*.md'):
        for href in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if href.startswith(('https:', 'http:', '#', 'mailto:')):
                continue
            target = (p.parent / href.split('#')[0]).resolve()
            if not target.is_relative_to(package.resolve()) or not target.exists():
                failures.append(str(p.relative_to(package)) + ' -> ' + href)
    if failures:
        raise ValueError('參考連結缺漏：\n' + '\n'.join(failures))


def build(lin, output):
    if output.exists():
        raise ValueError('輸出已存在，不覆蓋：' + str(output))
    sources = {'workflow': revision(ROOT), 'lin': revision(lin)}
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        package = Path(temp) / NAME
        prepare(package, lin)
        validate(package)
        checksums = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(package.rglob('*')) if p.is_file()}
        (package / 'SOURCE.json').write_text(json.dumps(
            {'built_at': datetime.now(ZoneInfo('Asia/Taipei')).isoformat(),
             'sources': sources, 'files': checksums}, ensure_ascii=False, indent=2) + '\n')
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
            for p in sorted(package.rglob('*')):
                if p.is_file():
                    archive.write(p, p.relative_to(package.parent))
        with zipfile.ZipFile(output) as archive:
            assert archive.testzip() is None
        print(f'已建立並驗證：{output}（{output.stat().st_size:,} bytes）')
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lin-source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    build(args.lin_source.expanduser().resolve(), args.output.expanduser().resolve())
