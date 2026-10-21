# 維護者｜Skill 設定與安裝

設計師教學以已完成設定的 Claude 帳號或團隊空間為前提，不要求同事下載 Skill 包或逐案安裝。以下為維護者保留的設定、打包及本機維護說明。

若同事使用不同帳號，需完成分享或組織配置，並確認對方已可使用；只上傳到維護者個人帳號不會自動對所有人開放。可依 [Claude 官方 Skill 說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)設定。

現行製作流程只有 `visual-solution-immersive-director` 一個主 Skill。`eagle` 與 `eagle-visual-solution-curator` 是團隊共用的資源庫工具，會一起安裝，但不是網站製作角色。

套件另附 8 個 `gsap-*` 技術 Skills：core、timeline、scrolltrigger、performance、plugins、utils、react、frameworks。安裝程式會一併安裝，主 Skill 按需讀取，不會每次全部載入，也不會安裝 GSAP JavaScript 套件。來源與使用界線見 [GSAP 技術 Skills](skills/visual-solution-immersive-director/references/gsap-skills.md)。只搬主 Skill 資料夾會缺少這些參考，請安裝整包。

安裝由使用者要求時執行。有兩種方式：**Claude Code 用 Plugin**，**Codex 用 install.py**。同一台電腦的 Claude Code 只選一種，兩種都裝會出現兩份 Skill。

## Claude Code：Plugin（建議）

GitHub 帳號需先被加為協作者，且這台電腦的 git 已能存取私人 repo（能 clone 就可以）。在 Claude Code 輸入：

```text
/plugin marketplace add world-yingcen/Visual-Solution-Workflow
/plugin install visual-solution@visual-solution-workflow
```

完成後重新載入，Skill 名稱會帶前綴，例如 `/visual-solution:visual-solution-immersive-director`。一次裝好主 Skill、8 個 GSAP 與 2 個 Eagle 工具，不需要 Python，也不用固定資料夾。

更新：自建 marketplace 預設不自動更新。到 `/plugin` → Marketplaces → 開啟 Enable auto-update；或手動執行 `/plugin marketplace update visual-solution-workflow`。移除：`/plugin uninstall visual-solution@visual-solution-workflow`。

之前用 install.py 裝在 `~/.claude/skills` 的人，先在套件資料夾執行 `python3 install.py --status` 核對，再 `python3 install.py --uninstall`，然後改裝 Plugin。

## Codex（或不用 Plugin 時）：install.py

主 Skill 在每次開始或接續案件時會自動執行一次 `--update` 保持最新；其他時候不自動安裝依賴或修改權限。

把 repo clone 到本機固定資料夾（每台電腦各一份，不放雲端硬碟；GitHub 帳號需先被加為協作者），套件在 `skill/` 子資料夾，指令都在那裡執行。需要 Python 3.9 以上：

```bash
git clone https://github.com/world-yingcen/Visual-Solution-Workflow.git
cd Visual-Solution-Workflow/skill
python3 install.py --dry-run
python3 install.py
python3 install.py --status
```

預設安裝到 `~/.claude/skills`；Codex 指定目標：

```bash
python3 install.py --target ~/.codex/skills
```

預設建立捷徑指向套件資料夾，改 repo 即生效，所以資料夾不要搬；Windows 無法建捷徑時自動改用複製。拿到 zip 而非 clone 的人加 `--copy`，複製安裝在來源更新後需重新執行。同名非本安裝器管理的資料夾會跳過，不自動覆蓋。完成後在對應執行端重新載入 Skill。

安裝器只處理這份套件明列的主 Skill、8 個 GSAP 技術支援與 2 個 Eagle 工具；即使 `skills/` 內另有資料夾，也不會順便安裝。Eagle Skill 的安裝不會另外安裝 Eagle 應用程式；團隊電腦既有的 Eagle 仍須在使用時保持開啟。

`--update` 會取得 repo 更新並同步安裝；主 Skill 每次開始或接續案件會自動執行一次，使用者也可自行執行。Codex 請使用 `python3 install.py --update --target ~/.codex/skills`，避免更新到預設的 Claude 技能目錄。若在受限案件工作區出現 `.git/FETCH_HEAD: Operation not permitted`，是該執行環境不能寫入案件外的來源庫；核對來源庫狀態後，取得執行環境的寫入核准再重跑，不要改檔案權限或重置 Git。沒有網路、不是 git clone 或本機分歧時，既有安裝不受影響。`--uninstall` 依安裝紀錄移除該工具管理的項目，執行前先核對 `--status`。`--case` 是舊版 Claude 案件權限設定相容功能，並非使用主 Skill 的必要步驟；只有明確要求該設定時才使用。

既有舊角色安裝不會自動刪除；若要清理，先核對安裝位置與來源，再另外處理。工程工具依案件實際需要準備，不要求每案固定安裝 Sass、Node、Eagle 或 VS Code。

## Lin-EVO 共用規範（必要依賴）

切版／校稿及 EVO 轉換另需安裝 [lin-skill](https://github.com/world-yingcen/lin-skill) 的 Lin-EVO＋Miffy-EVO。此整體視覺套件／Plugin 不內含工程條文副本；請 clone 獨立 repo，依其 README 安裝兩個 Skill，並核對 `Miffy-EVO/evomni-html/` 的 VERSION、規範、範例與檢查器。Lin／Miffy 共用同一份工程師套件；工程師套件由人工更新，不以 Git 更新成功推定其為工程師最新版。缺少或更新失敗必須回報。方案設計流程與 RWD 範圍不變。

## Claude 網頁／App：Lin-EVO＋Miffy-EVO 整合包

維護者可使用 repo 根目錄的 `dist/claude-upload/Lin-EVO-Miffy-EVO-20261022.zip`，來自獨立 lin-skill 的同一份來源，含工程師 `evomni-html 1.1.0`。啟用後可用「使用 Lin-EVO」或「使用 Miffy-EVO」分流；停用舊版獨立 Lin／Miffy 上傳包。整體視覺流程另啟用 `dist/claude-upload/Visual-Solution-Workflow-20261022.zip`。這兩包包含工作前 Git 檢查、換電腦前 commit／push 與已轉 EVO 後停用原 Git 的最新規則。

本機 Codex／Claude Code 安裝與 Claude App 雲端上傳是不同位置。安裝器同步成功，不代表雲端 Skill 已更新；需在 Claude App 重新上傳這兩包、啟用新版並停用舊版，於新對話確認能讀取新版規則。

維護者核對獨立來源後，在本 repo 根目錄執行（替換實際來源與日期）：

```bash
python3 scripts/build_evo_upload.py --source /你的本機路徑/lin-skill --output dist/claude-upload/Lin-EVO-Miffy-EVO-YYYYMMDD.zip
```

打包器只讀來源；將 Lin／Miffy 入口轉為包內指南，保留工程師套件原檔，核對參考連結、套件逐檔一致及 ZIP 完整性，並將來源 commit、版本與雜湊寫入 SOURCE.json。不覆蓋既有包，不安裝或推送。這是 Skill 上傳包，不是客戶網站匯入 ZIP。

工程師提供新版時先依 Miffy 規範人工更新來源，再重建整合包並更新受管理帳號或組織的 Skill 設定。打包檢查不代表已通過 Claude 實際上傳或案件後台驗收。網頁／App 沒有本機檔案或內網存取能力時，需提供案件檔案；無法執行檢查器時依清單檢核後交後台預檢，不能偽造檢查報告。

## Claude 網頁／App：專用上傳 ZIP

Claude 網頁／App 的 Customize → Skills → Upload a skill 使用專用包；不要上傳整個維護 repo，也不要將上方 install.py 分享包當成單一上傳 Skill。維護者在 repo 根目錄執行：

```bash
python3 scripts/build_claude_upload.py \
  --output dist/claude-upload/Visual-Solution-Workflow-日期.zip
```

檔名日期換成本次日期；同名輸出已存在時不覆蓋。Skill 名稱為 `Visual-Solution-Workflow`，產物只有一個同名根資料夾與入口 SKILL.md，僅附 workflow 的流程參考。Lin-EVO 與 GSAP 由使用者另外上傳／啟用，本包不重複內附；Eagle 與系統 CSS 也不打包。SOURCE.json 記錄 workflow commit、外部 Skill 依賴與各檔案雜湊。打包器檢查內部連結、ZIP 完整性，排除 Git、安裝器、案例與其他本機資料。

2026-10-14 上傳版由 `visual-solution-cloud` 更名為 `Visual-Solution-Workflow`；舊整合包與舊名 workflow-only 包均改用新的同名 ZIP。已獨立上傳 Lin-EVO／GSAP 的使用者不需要重複內附這些 Skill。

此包優先套用網頁／App 環境規則，不要求本機安裝、Git 更新、Chrome 或 Eagle 連線。使用者須提供案件檔案；未接入工具或無法存取內網時列缺口，不宣稱已在本機或正式後台驗證。上傳後啟用 Skill，另以本案需求測試；打包檢查不代表已通過 Claude 實際上傳／執行。來源更新後由維護者重新打包並重新上傳，不會自動追蹤本機 Git。
