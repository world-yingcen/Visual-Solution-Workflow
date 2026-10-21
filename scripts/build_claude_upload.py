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
NAME = 'Visual-Solution-Workflow'
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


def prepare(package):
    resources = package / 'resources'
    workflow = resources / 'workflow'
    copy_guide(ROOT / 'skill/skills/visual-solution-immersive-director', workflow)

    p = workflow / 'GUIDE.md'
    text = p.read_text()
    text = between(text, '每次開始新一輪工作', '遇到 PDF 時',
                   '此為 Claude 網頁／App 上傳快照。每輪先重讀本包規範與已提供的案件進度；'
                   '不執行本機 install.py、Plugin 安裝或套件來源 Git 更新。'
                   '原始來源維護仍用 Git，更新上傳版須重新打包並上傳。'
                   '這不免除案件工作前的 Git 檢查：有實際案件 Git 工具時依工作前規則 fetch 與核對版本；'
                   '缺工具則說明限制並詢問是否需要帶著操作，不把快照當遠端最新版。'
                   '已轉 EVO 停用的原靜態 Git 不再更新或推送。')
    text = text.replace('使用本執行端的 Lin-EVO 更新並重讀共用規範',
                        '使用本次已啟用的獨立 Lin-EVO Skill 與本輪對應參考')
    # Keep the maintained Claude/manual-image division unchanged.
    p.write_text(text)

    (workflow / 'references/frontend-standards.md').write_text(
        '# 共用切版規範｜使用者獨立上傳的 Lin-EVO\n\n'
        '本 workflow 包不內附 Lin-EVO。使用者已另行上傳並啟用 Lin-EVO Skill；'
        '切版／修改／校稿時先確認本對話可使用該 Skill，再依其工程規範執行。'
        '以實際可用 Skill 名稱與內容為準，不猜另一個上傳包的檔案路徑。\n\n'
        'Lin-EVO 管 HTML／SCSS／JS、SEO、系統搜尋／詢問車、套件接入、雙模式動態與工程師交接。'
        '不要從此包舊摘要自行複製一份工程規則取代 Lin-EVO。'
        '如果執行端確實有本機安裝能力，缺少本輪需要的 Skill 時使用者已授權從已確認來源直接安裝。'
        '若當次無法取得 Lin-EVO，先完成品牌／視覺／動態提案等不受影響工作，'
        '明列工程規範缺口，請使用者確認已啟用或提供規範；不虛構已讀取。\n\n'
        'workflow 的品牌方向、確認關卡與 2560×1280 桌機優先仍有效。'
        '沒有平台資料或正式環境時記錄待驗，不要求本機安裝或 Skill 來源 Git 更新。\n')

    (workflow / 'references/gsap-skills.md').write_text(
        '# GSAP｜使用者分別上傳的技術 Skills\n\n'
        '本包不內附 GSAP。使用者會分別上傳並啟用，依實際可用清單按需使用；'
        '不要求安裝本機套件、不猜其他上傳包路徑、不宣稱每輪已載入全部。\n\n'
        '| 需求 | 對應 Skill |\n|---|---|\n'
        '| 基本動畫、easing、matchMedia | gsap-core |\n'
        '| 時間軸與連續轉場 | gsap-timeline |\n'
        '| 捲動、pin、scrub | gsap-scrolltrigger |\n'
        '| 效能 | gsap-performance |\n'
        '| 額外 plugin | gsap-plugins |\n'
        '| 數值工具 | gsap-utils |\n'
        '| 已有 React／Next.js | gsap-react |\n'
        '| 已有 Vue／Nuxt／Svelte | gsap-frameworks |\n\n'
        '沿用案件實際 GSAP 版本，技術範例不取代 Lin-EVO 結構與品牌分鏡。'
        '缺相關 Skill 時明列尚未取得，先完成可做的規劃或查已授權官方資料；'
        '不自行加入框架、效果或套件。')

    # Embedded guides are resources, not additional independently installed Skills.
    for p in package.rglob('*.md'):
        text = p.read_text()
        text = text.replace('先讀同套件的 [Eagle 工具規則](../../eagle/SKILL.md)',
                            '先讀本次已啟用的 Eagle Skill／工具文件（本包不內附，不能猜另一包路徑）')
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
name: Visual-Solution-Workflow
description: 在 Claude 網頁／App 依品牌資料規劃與製作整體視覺網站，專注品牌、視覺、動態提案與確認流程，切版與動畫技術使用另外啟用的 Lin-EVO／GSAP Skills；適用提案、製作及續作。
---

# Visual-Solution-Workflow

整體視覺網站流程｜Claude 網頁／App 上傳版

以繁體中文與台灣用語協作。先讀 [整體視覺主流程](resources/workflow/GUIDE.md)，
切版／修改／校稿依使用者另外啟用的 Lin-EVO；動畫技術按需使用獨立 GSAP Skills。
resources 內的 GUIDE.md 都是本包參考，不是需要另外安裝的 Skill。

## 此上傳環境的優先規則

本節優先於參考中僅適用本機的安裝、更新、工具或派工指令；
品牌、設計、工程與使用者已確認規格仍保留，不擅自降低交付要求。

- 這是來源版本快照，不能自動連到使用者本機 Git 或追蹤 GitHub 最新版。
  每輪重讀本包與案件進度；更新規則需由維護者重新打包、由使用者重新上傳。
  不執行快照中的本機安裝器、Plugin 更新或本機清理；案件 Git 與後台操作另依實際工具及本次授權。
- 只讀對話已提供或工具已授權可存取的檔案。不能直接讀使用者的 /Users 路徑、
  Google Drive 同步資料夾、公司內網或 localhost。需要來源時請使用者提供相關
  HTML／CSS／JS、文字或重點截圖；連結能否存取以本次工具結果為準。
- 本包只內附 workflow 流程參考，不內附 Lin-EVO、GSAP、Eagle 或系統搜尋 CSS。
  工程規範使用另外啟用的 Lin-EVO，動畫技術使用獨立 GSAP Skills。
  沒有本案後台、evomni-page-composer 或客戶素材，不能編造平台 API／資料綁定。
- 案件全程使用 Claude App；素材由 Claude 提供 prompt，使用者至 ChatGPT 產圖，
  下載後放入本案 image/，自行處理 WebP 與容量，再由 Lin 更新引用並檢查。
  不自動派工 Codex 或操作 ChatGPT 產圖；Eagle／瀏覽器僅在可用且授權範圍內查看參考。
- 使用者已授權本機缺少本輪相關 Skill 時，從已確認來源直接安裝，
  不逐次請示、不覆蓋同名衝突或本機修改；但沒有本機安裝工具的網頁／App
  不能假裝已安裝，改用已啟用 Skill 或提供明確上傳方式。
  此授權不涵蓋應用程式、JS 套件、工程工具庫與系統權限變更。
- 有程式執行能力才處理已提供的工程；有瀏覽器才實看、實測。
  缺能力時提供可下載成果與驗收步驟，明列未驗證，不宣稱已測通過。
  預設第一階段 2560×1280 桌機；已依操作手冊指定桌機後做 RWD 時，確認後直接接續。
- 尚未轉 EVO 的 Git 切版案件，換電腦前先確認範圍與是否需帶操，完成 commit 並 push；
  另一台取得同一版本後先讀交接。已轉 EVO 的案件改至後台，原靜態 Git 不再修改或 push。
- 單一 PDF 超過 10 MB 一律不讀，請提供重點截圖或 .md；未超過上限先問
  現在讀或用到再讀。圖片容量與格式要檢查，轉檔／壓縮由使用者自行處理。
- 工程、SEO、系統公版功能、雙模式動態與工程師交接細則由獨立 Lin-EVO 維護；
  本包不複製另一份。不因缺工具就宣稱已套用或驗證；保留 workflow 的確認關卡。

## 獨立依賴的使用方式

- [Lin-EVO 接入說明](resources/workflow/references/frontend-standards.md)
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


def build(output):
    if output.exists():
        raise ValueError('輸出已存在，不覆蓋：' + str(output))
    sources = {'workflow': revision(ROOT)}
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        package = Path(temp) / NAME
        prepare(package)
        validate(package)
        checksums = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(package.rglob('*')) if p.is_file()}
        (package / 'SOURCE.json').write_text(json.dumps(
            {'built_at': datetime.now(ZoneInfo('Asia/Taipei')).isoformat(),
             'sources': sources, 'external_skills': ['Lin-EVO', 'Miffy-EVO', 'gsap-*'], 'files': checksums}, ensure_ascii=False, indent=2) + '\n')
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
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    build(args.output.expanduser().resolve())
