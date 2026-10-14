# 2026-10-14｜EVO Skills 與 workflow 維護交接

## 新對話接續指令

```text
請先讀 docs/codex-handoffs/2026-10-14-evo-skills-workflow.md、AGENTS.md 及本次涉及目錄的規則。
核對兩個 repo 的 Git 狀態與本機 Skill 安裝，依文件接續；不要重新建立規範或覆蓋未提交修改。
Visual-Solution-Workflow 是 Claude 網頁／App 上傳入口；Lin-EVO 負責切版，Miffy-EVO 負責靜態版轉 EVO。
本機整體視覺入口仍是 visual-solution-immersive-director。
本次工作：（填下一個需求）。
```

## 目前目標與完成狀態

本輪是 Skill 規範、名稱、打包及教學維護，未啟動客戶案件，也未修改實際客戶網站、正式後台或部署。
截至本文件建立前，今日相關內容已提交並推送；本文件另提交推送。沒有需要接著執行的客戶製作工作。

| 來源 | 本機位置 | 分支／已推送版本 |
|---|---|---|
| workflow | `/Users/wd-t160/LINS/git/Visual-Solution-Workflow` | `main`；`a2cc682` 教學更新，之前 `849255a` 新 Skill 引用／上傳包、`03cb8fc` workflow 上傳名稱 |
| EVO Skills | `/Users/wd-t160/LINS/git/skills/lin-skill` | `main`；`f44176b` 改名與安裝遷移，之前 `ea2a2e3` 修正公版適用範圍 |

使用者授權更新檢查完成後 commit／push，不能因此自動部署、發布客戶網站或修改其他案件。

## 已確認名稱與分工

- `Visual-Solution-Workflow`：Claude 網頁／App ZIP 的 `name`、根資料夾與入口標題，大小寫按使用者指定。
- 本機 workflow 的 `visual-solution-immersive-director` 未改名；不要將兩種環境的入口混用。
- `Lin-EVO`：原 lin-frontend，負責設計稿切版、HTML／SCSS／JS、共用頁面、SEO、動態與交接。
- `Miffy-EVO`：原 miffy，負責已完成靜態頁面轉 EVO、匯入包、可編輯資料與接入驗證。
- 兩個來源資料夾、Skill frontmatter、agents 顯示名稱／提示、README、安裝 CLI 及有效 workflow 引用已改名。
- workflow 上傳包只包含 workflow，不內附 Lin-EVO、Miffy-EVO、GSAP、Eagle 或系統搜尋 CSS；工程與動畫技術按需啟用獨立 Skill，避免複製兩份工程規範。
- 歷史教學備份與舊產物不是現行入口，不為改名重寫歷史快照。安裝程式保留舊名稱字串作遷移相容，不能將其當漏改。

## 本機安裝與更新

- Codex 的 `Lin-EVO` 與 Claude 的 `Lin-EVO` 是連到獨立 Git 來源的捷徑；修改來源直接生效。
- Codex 的 `Miffy-EVO` 保留原有受管理副本模式，改名後已同步；本輪未新增 Claude 的 Miffy-EVO 安裝。
- 安裝器遷移舊捷徑／副本及各自 manifest；保留原模式。來源不同、舊副本自行修改、新舊名稱同時存在時停止，不覆蓋。
- 本機啟用前偵測 Git 就安全更新；不 reset、stash、force push 或抹掉本地修改。上傳 ZIP 是快照，不能假裝自動 Git 更新。
- 使用者已授權：本機缺本輪相關 Skill，可從已確認來源直接安裝；不擴及應用程式、JS 套件、工程工具庫或系統權限。
- Miffy-EVO 每次轉換前核對工程工具庫與本案版本；缺公司內網、VPN、後台或工具能力時列具體缺口，不宣稱已驗證。

## 公版修改範圍：以最後澄清為準

1. **詢問車頁／詢問抽屜及搜尋頁**：CSS 可依案件確認需求調整，公版 HTML／JS 不改；不是所有產品頁或所有公版元件全面禁止修改。
2. **產品頁**：切版端可以新增獨立 `.inquiry-group` div、調整加入詢問單位置，不需列工程師待改；放在購買按鈕群下方、商品資訊最下面，保留原生 class／data、平台資料及加入功能綁定。
3. **分類選單**：沿用 `left_menu001` 結構與必要識別。桌機外觀保留案件設計，手機版下拉操作邏輯是公版，不改寫或另綁一套事件。文字導頁、箭頭獨立展開、目前分類標籤、無子分類不顯示箭頭、展開清單不得被 Footer 遮住。
4. 案件選單樣式集中 `_left-menu.scss` 或既有相同用途檔案，在公版 CSS 後載入；公版原始檔保留。第一列箭頭偏移先查 margin 合併，確認根因才用 flow-root，不硬改第一列 top。
5. `1199px`、padding、18px 箭頭、sticky／圓角白底／米色標題／選取圓點、`container-75`、字級倍率及配色是案件確認值，可按案覆蓋，不強制所有網站相同。
6. Header「立即購買」依案件在產品內頁／詢問頁隱藏（含手機置底），列表／分類保留；先確認按鈕用途，不全站誤藏 `.header-btn-link`。
7. 加入成功沿用原生 `EvomniAlert`「已加入詢問單」及來源的 4 秒，不自行換 toast；抽屜不能被 Cookie 蓋住。修改原生 focus 的 `preventScroll` 是工程師待修建議，未實作不得寫完成。
8. 靜態 Demo 經使用者要求可獨立模擬加入、跨頁保存、數量、移除／表單，不呼叫正式 API、不真的寄出，不偽造正式平台 ID。正式接入前排除 Demo 及示範資料，只綁原生操作；有產頁腳本須同步。
9. 搜尋頁每案必備。HTML／JS 沿用公版，CSS 未指定調整時忠實沿用參考；不能只用同名 class 卻自創標題／摘要／按鈕。附帶搜尋 CSS 已收齊來源與後載入覆寫。

最初把不可修改限制推到全部公版、將 `.inquiry-group` 列工程師待辦的解讀已撤回，勿再引用。

## 其他已納入規範的責任

- PDF 先檢查大小：單一超過 10 MB（10,000,000 bytes）一律不讀，改請提供重點截圖或 Markdown；其餘先問現在讀或用到再讀，待用文件獨立整理並註明未讀。
- 切版完成提醒使用者檢核專案容量，列非 WebP／SVG 圖片路徑與大小；WebP／SVG 也查容量。使用者自行轉檔／壓縮，AI 不代做。教學原有「AI 壓縮」字句已修正。
- Navi 才能用 `<header>`；完整頁面只有一個 h1 是公司內部規定，h2～h6 依資訊層級。逐頁核對 title、描述、圖片 alt／尺寸、真實連結及載入；正式網址、索引及後台設定交工程師確認。
- EVO 平台套件不自行加 CDN／script／link：Swiper、GLightbox、已確認開放的 Lenis 使用 data-vendor；宣告負責載入、版型 JS 負責初始化。Lenis 在本案平台是否已更新開放須另查，不預設全部可用。GSAP／AOS 由編輯器工具列開啟。
- 一般／減少動態模式都要完成，減少動態仍完整呈現內容、正常閱讀與操作；GSAP pin／scrub 解除固定、疊層與留白，不只 early return 或把 timeline 強跳最後一格。模式切換清理自有實例，不全域 killAll。未核准不新增訪客動畫開關。
- 切版完成及功能修改要同步唯一 `工程師交接說明.md`，記已完成／待接入／未實測／Demo 停用、檔案載入與產頁腳本。文件完成不等於正式接入完成。
- workflow 預設 2560×1280 桌機，RWD 待授權；教學的完整製作啟動指令已明確包含桌機確認後接 RWD，按該案已授權範圍執行，不因 Skill 預設漏做。

## 可用上傳包

都位於 workflow repo 的 `dist/claude-upload/`，名稱／ZIP 根資料夾已核對：

- `Visual-Solution-Workflow-20261014-EVO.zip`：約 91 KB，依賴 Lin-EVO／GSAP，無工程規則副本。
- `Lin-EVO-20261014.zip`：約 77 KB，含完整工程規範及搜尋 CSS。
- `Miffy-EVO-20261014.zip`：約 17 KB，含轉換規範。

這些是結構／內容／ZIP 檢查通過，不代表已在 Claude App 完成實際上傳與執行。使用者需重傳新版、停用舊入口。大小寫依使用者指定保留，未驗證 Claude 平台是否有其他名稱限制；若平台拒絕，以實際錯誤處理，不擅改名。

## 教學更新與檔案位置

`skill/使用教學.md` 與 `skill/使用教學.html` 同步新增環境差異、上傳包／開始方式、切版共同檢查、交接責任與 Miffy-EVO 轉換。

`skill/index.html`、`skill/快速索引.md`／`.html`、`skill/guide-tools.html`、`skill/README.md` 同步入口與新名稱；把誤稱維護者為 Lin-EVO 的字句修正。詳細工程條文仍由獨立 EVO Skills 維護。

主要 source：`scripts/build_claude_upload.py`、`skill/INSTALL.md`、`skill/skills/visual-solution-immersive-director/references/frontend-standards.md`；獨立來源的 `Lin-EVO/references/evo-inquiry-cart-reference.md`、`evo-left-menu-reference.md`、`evo-search-reference.md`、`engineer-handoff.md` 及 `install.py`／`tests/test_install.py`。

## 已執行驗證

- 獨立 Skill 安裝器 24 項 unittest 通過，包含名稱遷移、受管理副本／連結、保護自行修改、試跑與更新安全檢查。
- 本機 Codex 兩個 Skill 與 Claude Lin-EVO 安裝狀態一致；獨立 Skill repo 無未提交修改。
- Skill frontmatter 的 name 與資料夾一致、Markdown 相對連結有效；ZIP 完整性及 workflow SOURCE.json 各檔雜湊檢查通過。
- 教學四個 HTML 頁的本機連結／章節錨點、唯一 id、單一 h1 檢查通過。
- 教學新增章節已在瀏覽器預覽，342px 寬無水平溢出，章節導航能到切版檢查；不是所有裝置尺寸完整驗收。
- 相關 commit 推送後核對本機 HEAD 與遠端 main 一致。客戶頁面、後台／正式搜尋／詢問送出、Claude App 實際執行均不在本輪驗證內。

## 未提交變更：保留現況

建立此文件時 workflow 工作目錄仍有以下先前變更，不混入本次 handoff 提交：

- 刪除 `dist/claude-upload/Visual-Solution-Workflow-20261014.zip`（舊上傳名產物）。
- 刪除 `dist/claude-upload/visual-solution-cloud-workflow-only-20261014.zip`（更早上傳名產物）。
- 刪除 `lin-skill/README.md`（workflow 內的舊入口）。
- `skill/快速索引.html` 的 intro 簡化為「依情境選擇／找到你的下一步」，移除舊介紹文案。

這些變更來源未在本輪確認；前幾次提交均保留，不還原、不擅自 stage 或永久刪除。下次先詢問／核對原意再決定是否提交。歷史 backups 也不為清理而修改。

## 下次接續

1. 先讀 handoff 與 repo 規則，檢查兩個 repo／本機安裝，保留上述未提交變更。
2. 若使用者已上傳三份 ZIP，取得實際使用回報；若尚未上傳，提供現有新版包，不重複重建內容相同的包。
3. 依本次新需求再修改規範或教學；需要上傳快照更新時重新打包，不假裝雲端自動同步。
4. 若要收尾舊產物刪除／快速索引版面，先核對使用者原意並將那部分單獨提交。
5. 遇平台接入需求，先取得本案來源與版本，再按最後確認的公版界線實作；不把本輪文件維護當客戶網站已修好。

不安排背景任務、不清理 Codex、不封存對話，也不操作其他 repo／案件。使用者本輪只是要求下班前保存交接並 push。
