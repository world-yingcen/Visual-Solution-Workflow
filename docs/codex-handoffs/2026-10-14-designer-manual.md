# 設計師操作手冊｜2026-10-14 交接

## 接續提示

```text
繼續完成這個 repo 的設計師教學文件。先讀 docs/codex-handoffs/2026-10-14-designer-manual.md、AGENTS.md 與 skill/AGENTS.md，再查看目前 Git 狀態及最新文件，確認哪些內容仍適用。不要依賴舊聊天記憶。
優先沿用四頁共用樣式與互動，依使用者指定區塊直接修改。需要預覽時啟動 skill/ 的本機伺服器，開啟教學入口或使用須知。修改流程文件不代表開始客戶案件、安裝工具或部署。
```

## 專案與交接狀態

- Repo：`Visual-Solution-Workflow`，本機位置 `/Users/wd-t160/LINS/git/Visual-Solution-Workflow`。
- 分支：`main`；遠端：`https://github.com/world-yingcen/Visual-Solution-Workflow.git`。
- 本次整理前 HEAD：`a2cc682`，`Update designer tutorials for renamed skills and EVO delivery rules`。
- 目標：做成設計師可直接操作的圖文手冊，包含完整流程、依情境入口與使用須知；目前可用，仍可接續校閱內容。
- 使用者本次明確要求「打包 handoff，下班了，然後 push 上去」。交接文件、最後標題調整及已存在的舊檔刪除一起提交並推送。提交編號與推送結果請看本文件之後的 Git 紀錄。
- 只整理 repo 交接；沒有清理 Codex 狀態、封存聊天或建立排程。

## 四頁與共用檔案

| 檔案 | 用途 |
| --- | --- |
| `skill/index.html` | 教學入口，兩張卡片：完整流程／依情境 |
| `skill/使用教學.html`、`skill/使用教學.md` | 按順序完成操作的手冊 |
| `skill/快速索引.html`、`skill/快速索引.md` | 六種情境的資料準備與可複製指令 |
| `skill/guide-tools.html` | 使用須知，從舊版圖文教學整理出的觀念、確認點與工具說明 |
| `skill/css/manual.css` | 四頁共用 CSS、深淺色、頁首、圖文元件、情境卡片與回到頂部 |
| `skill/js/copy-code.js` | 複製指令；支援原生剪貼簿與替代方式 |
| `skill/js/scroll-top.js` | 四頁右下角共用回到頂部按鈕 |
| `scripts/build_share_package.py` | 分享包清單：四頁、共用檔與指定案例資源 |
| `scripts/build_claude_upload.py` | Claude 上傳包工具；與教學分享包不同 |

四頁頁首名稱統一為「方案產業AI化_操作手冊」，`.guide-tools` 內包含教學入口、完整流程、依情境、使用須知與主題切換。

## 已完成的教學及視覺決定

1. 原先偏好的圖文版本位於 `docs/tutorial-backups/2026-10-09-before-beginner/skill/使用教學.html`；保留為歷史備份，不直接覆寫。
2. 完整流程與情境索引放在同一專案，由入口頁分成兩種閱讀方式。使用須知另開一頁，保留分工、五個確認點圖解、Eagle、資料夾／進度、模型選擇、FAQ 與問題處理；操作步驟連到現行完整流程。
3. 四頁共用樣式，沒有各頁獨立複製 CSS。深色 `--surface: #2f2f2f`；桌機 h1 為 70px、bold，小螢幕保留已確認的較小字級。
4. 入口的主標題與兩張卡片置中，卡片使用完整寬度的綠色／琥珀色圓角按鈕。保留兩種入口，不增加第三張卡片；使用須知由頁首進入。
5. 六種情境：從零開始、Webtech2 首頁重切、靜態首頁接內頁、高效初版交設計師優化、Figma／設計稿切版、修改與問題修正。Webtech2 情境要求依新切版規範重切視覺相同的靜態 HTML，再延伸內頁。
6. 手冊明確包含桌機內部確認後接續 RWD，完整檢查後再交客戶校稿；因此沒有單獨的 RWD 情境。不要將這個教學約定無條件改成所有案件的 Skill 預設範圍。
7. 最新情境頁 h1 是「依情境選擇／找到你的下一步」。已刪除該頁 `intro-meta` 日期列與 `intro-description`，也刪除指定的「RWD 已併入製作流程…」提示；上方製作順序圖仍保留。
8. 完整流程曾刪除「先看這裡｜工作入口」、「整理客戶回饋與確認版本」區塊及指定的介紹日期。不要無意加回。
9. 「當你收到修改資料時」是獨立第 11 步（`#revisions`），「整理靜態網站交付」順延第 12 步（`#delivery`），導覽與 Markdown 同步。
10. 指令右上角有一鍵複製。`.copy-block pre` 的 `margin: 0; padding-top: 20px; padding-right: 70px;` 是使用者指定值。
11. 回到頂部按鈕下滑 320px 後顯示，桌機右／下 24px、手機 16px，兼顧安全區；平滑捲動，減少動態時直接回頂，並把鍵盤焦點帶回主內容。

## 提案與動態分鏡案例

- `skill/Ocean-Medi-歐群生醫/`：原視覺提案、Banner 分鏡及資源。第 4 步展示提案預覽；第 5 步展示起始／移動中／停留，可連回原頁切換狀態。
- `skill/Ichia-毅嘉科技/`：原視覺提案與動態腳本、產品素材。第 4 步展示首頁構圖；第 5 步選 Scene B 模組換層的起始／過程／結束，並連回完整腳本。
- 實際瀏覽器擷取的預覽圖在 `skill/examples/ocean-medi/` 與 `skill/examples/ichia/`，不是生成圖。
- 案例使用 `.tutorial-example`、`.example-preview`、`.example-frames` 等共用元件；手機分鏡改成單欄。
- 分享包按 `TUTORIAL_FILES` 固定清單收錄 54 個案例／預覽檔案，不掃描其他客戶案件。
- 案例是歷史提案展示，不代表其他案件的品牌方向、既有確認範圍或已實作動畫。

## 現行內容與先前討論的差異（以最新 repo 為準）

本次整理發現，其他已提交更新已調整名稱、PDF 與 EVO 說明。以下是目前檔案的事實，不回退到聊天早期版本：

- 本機整體視覺主入口仍為 `visual-solution-immersive-director`；Claude 網頁／App 上傳入口為 `Visual-Solution-Workflow`。原 `lin-frontend`／`miffy` 現在使用 `Lin-EVO`／`Miffy-EVO`。
- 現行 `#skill-environment` 有環境差異與上傳包說明；網頁／App 不假設可讀本機路徑、localhost、公司內網或 Eagle。
- 前期要求移除 PDF 已被後續已提交規則取代：PDF 可保留，先確認現在讀或用到再讀；單檔超過 10 MB（10,000,000 bytes）拒絕讀取，請提供重點截圖或 Markdown。待用 PDF 放在 `04_型錄與原始素材/PDF_待用時讀取/`。
- 前期曾移除 EVO 轉換；最新 `a2cc682` 已重新加入 `#evo-transfer`（Miffy-EVO 接續）及 `#frontend-checklist`。不要僅憑舊聊天移除。這些更新的完整決策脈絡未在本次聊天展開；要調整時先讀現行規則。
- 現存有效上傳包：`Visual-Solution-Workflow-20261014-EVO.zip`、`Lin-EVO-20261014.zip`、`Miffy-EVO-20261014.zip`，皆在 `dist/claude-upload/`。
- 本次開始時已有兩份舊 ZIP 與 `lin-skill/README.md` 的刪除，已確認新版三份包仍在且手冊連結指向新版；一併提交清理成果，root README 移除「lin-skill/ 僅保留搬遷說明」的過期描述。

## 校稿與修改的已確認操作

- 專案提供的資料複製到自己的 Google Drive 同步案件資料夾，不直接在共用區工作；請 Skill 盤點整理，資料夾樹是示意，不強制重建既有工程。
- 第 10 步：效率雲開本案 Evomni 取得版號 → 本機建立／沿用 `project` → `project/案件版號/` 複製完整網站 → 依公司文件的情況 A 推到 Git → 效率雲 62 DEMO 取得外網連結。
- 公司文件：`http://posthub.miracle-single.tw/docsys/#/articles/publish/2335`。手冊保留使用者提供的三個 Apple 捷徑；未確認其具體名稱，因此仍顯示捷徑 1／2／3。
- 第 11 步：已有案件直接開資料夾；沒有就 VSCode 指令面板選 Git: Clone、貼公司 Git URL、選本機位置並自行登入。修改完成請 Claude 提交並 push 原 repo／分支，確認 62 DEMO 最新結果。
- 本機校稿網站副本與 Google Drive 的案件資料分開。帳密由使用者自行操作，不寫入聊天或交接。

## 驗證與限制

前續作已完成的瀏覽器檢查：

- 共享 CSS 抽離曾在四頁新增前，以原三頁 1440／768／390 比對截圖，確認外觀保持一致。
- 案例於 1440／768／390 檢查圖片與相對連結、原案例狀態切換，無缺圖／本機 404／JavaScript 錯誤。
- 使用須知新增後，四頁於 1440／768／390／320 檢查無橫向溢出；章節導覽、深淺色與一鍵複製正常。
- 回到頂部在四頁手機尺寸，以及桌機／鍵盤／一般與減少動態模式測試正常。

本次交接重新執行：

- `git fetch origin`；整理前 `HEAD...origin/main` 為 `0 0`。
- 四頁 HTML 的本機 `src`／`href`、內頁錨點及圖示參照檢查通過。
- `copy_package()` 複製到暫存目錄，四頁、共用 JS 與固定案例清單皆可完整打包；沒有為了 handoff 額外產生 ZIP。
- `git diff --check` 通過。

本次只有標題與說明刪除，未重新執行整套瀏覽器檢查，也未驗證遠端外部頁面、客戶案件、後台匯入或實際公開部署。頁面可用不代表內容已完成使用者最後校閱。

## 本機預覽

啟動方式：

```bash
python3 -m http.server 8767 --bind 127.0.0.1 --directory skill
```

入口：`http://127.0.0.1:8767/`；使用須知：`http://127.0.0.1:8767/guide-tools.html#basics`。

本次已啟動且取得 HTTP 200；程序是暫時狀態，下次先確認是否仍在執行。不要把開啟本機伺服器當成部署完成。

## 下一步

1. 讀交接與最新 Git 狀態，核對遠端提交與任何新變更；不要覆蓋其他工作的內容。
2. 啟動／重用預覽伺服器，讓使用者從入口或目前指定的頁面繼續校閱。
3. 依使用者下一項需求逐區修改；維持四頁共用 CSS、導覽、複製與回到頂部。
4. 校閱近期新增的環境／Lin-EVO／Miffy-EVO 說明是否與最新獨立規範一致；未知決策先標出，不自行回退。
5. 涉及手冊正文的變動同步 HTML／Markdown；新增資源時同步分享包固定清單。
6. 有版面或互動變更再做適量桌機／平板／手機驗證，完工後簡短回報。

## 工作偏好與不可擅改事項

- 一律繁體中文與台灣用語；視使用者為設計師／前端實作者，說明直接、避免堆工程術語。
- 資訊足夠就直接做，不反覆確認；修改前先讀既有結構，用最小必要調整。
- 不無故改框架、套件、原案例視覺／素材、動畫、RWD 或已確認數值。
- 不把歷史案例當成主 Skill 的規則，不把文件維護當成客戶開案。
- 不自動安裝／部署／產生客戶案件；Git 推送需有本次明確授權，本次已授權。
- 本地 QA 暫存腳本不屬於 repo 的正式測試；續作可依現有環境重建，不依賴暫存檔仍存在。
