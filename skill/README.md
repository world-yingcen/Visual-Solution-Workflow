# 整體視覺方案｜從這裡開始

不需要會寫程式。你負責準備資料、看預覽與給回饋，AI 負責製作與整理。

## 設計師請看

先開啟 [教學入口](index.html)，選擇閱讀方式：

- [使用須知](guide-tools.html)：圖文了解 Skill 分工、五個確認點、工具與常見問題。
- [完整流程](使用教學.html)：按順序了解各階段的操作與確認。
- [依情境](快速索引.html)：從目前已有成果找到準備資料與開始指令。

兩種方式都在同一份教學專案內，可隨時切換。另有 [完整流程文字版](使用教學.md)與 [情境文字版](快速索引.md)。

三頁統一載入 `css/manual.css`，教學指令的一鍵複製使用 `js/copy-code.js`。調整共用外觀時修改這份 CSS；複製或分享教學時，請一併保留 `css/` 與 `js/` 資料夾。

手冊涵蓋資料準備、工具分工、產圖、視覺與動態確認、完整網站、客戶校稿，以及靜態網站交付。已有設計稿只需切版時，使用獨立 Lin-EVO 教學。

桌機完成並經內部確認後，直接接續 RWD，完整檢查後再交客戶校稿；各情境的啟動指令已包含這項範圍，不需另選 RWD 情境。Webtech2 已完成首頁時，由 Lin-EVO 依新規範重切視覺相同的靜態網站，再延伸內頁。

第一次使用先請 維護者協助設定，之後照教學貼指令即可。不需要先讀工程規範。

## 維護人員請看

安裝與更新方式見 [INSTALL.md](INSTALL.md)，AI 工作規範見 [主 Skill](skills/visual-solution-immersive-director/SKILL.md)。

套件包含整體視覺主 Skill、8 支 GSAP 技術 Skills、Eagle 相關 Skills，以及手冊明列的歐群生醫、毅嘉科技視覺提案／動態分鏡示範與必要素材；不含其他客戶案件、案例資料庫或憑證。工程師提供的範本資料需另行取得。

歐群生醫與毅嘉科技案例連結放在手冊第 4、5 步，預覽圖分別放在 `examples/ocean-medi/`、`examples/ichia/`，原示範頁與所需資源在 `Ocean-Medi-歐群生醫/`、`Ichia-毅嘉科技/`。案例用於理解提案展示與確認方式，不構成其他案件的設計規則。

教學更新不代表已完成實際案件製作或客戶確認。

## Lin-EVO 共用規範（必要依賴）

切版／校稿另需安裝 [lin-skill](https://github.com/world-yingcen/lin-skill) 的完整 Lin-EVO。此套件／Plugin 不再內含工程條文副本，本機缺少本輪需要的 Lin-EVO 時，可依已授權來源安裝；網頁／App 則由使用者另外上傳。請 clone 獨立 repo，依其 README 安裝；每次使用由 Lin-EVO 執行安全更新與重讀。缺少或更新失敗必須回報，不能宣稱已最新。方案設計流程與 RWD 範圍不變。

## Claude 網頁／App 與新版切版檢查

上傳入口為 `Visual-Solution-Workflow`，切版為 `Lin-EVO`，靜態版轉 EVO 為 `Miffy-EVO`；本機整體視覺入口仍為 `visual-solution-immersive-director`。上傳包、環境差異與開始指令見 [手冊環境說明](使用教學.html#skill-environment)。

搜尋／詢問公版、分類選單、SEO、雙模式動態、圖片容量與工程師交接的操作提醒見 [切版共同檢查](使用教學.html#frontend-checklist)；轉換接續見 [Miffy-EVO 轉換](使用教學.html#evo-transfer)。詳細條文由獨立 Lin-EVO／Miffy-EVO 維護。
