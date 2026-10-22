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

## Lin-EVO 與 Miffy-EVO：來源及安裝

整體視覺套件／Plugin 不內附兩者的工程條文。切版與校稿使用 Lin-EVO，轉 EVO 使用 Miffy-EVO。

目前維護者本機配置（其他機器改用已確認的實際路徑）：

| 用途 | 位置 |
|---|---|
| 修改 Lin-EVO | `/Users/wd-t160/LINS/git/skills/lin-skill/Lin-EVO/` |
| 修改 Miffy-EVO | `/Users/wd-t160/LINS/git/skills/Miffy-EVO/` |
| 共用安裝器與路徑設定 | `/Users/wd-t160/LINS/git/skills/lin-skill/install.py`、`skill-sources.json` |
| 工程師 HTML 套件 | Miffy-EVO 裡的 `evomni-html/` |

Codex／Claude 本機目前直接連結上述來源；修改後下次讀取即可使用。核對各工具自己的安裝紀錄與實際連結，不能只看資料夾名稱。本機同步範例：

```bash
python3 /Users/wd-t160/LINS/git/skills/lin-skill/install.py --tool claude --skill Lin-EVO --link
python3 /Users/wd-t160/LINS/git/skills/lin-skill/install.py --tool claude --skill Miffy-EVO --link
```

Codex 改 `--tool codex`，安裝前核對來源及既有修改。部分拆分期間，舊整包 Git 更新已停用，同步不加 `--update`；不要把 Miffy 搬回舊位置或自行建立遠端。這不影響本 workflow 本身的 Git 更新，但 workflow 更新也不代表兩個外部 Skill 已更新。

Lin／Miffy 共用同一份工程師套件。每輪讀實際 VERSION、規範與檢查器；套件由人工更新，不以 Git 更新成功推定為工程師最新版。缺少來源或無法確認版本時明列限制。

## Claude 網頁／App：Lin-EVO＋Miffy-EVO 整合包

本機安裝與 Claude App 上傳是不同位置；來源改動後要重新打包及上傳才會生效。已產生的 ZIP 是歷次快照，不因本機搬移自動更新；不得只憑日期宣稱為最新。

維護者可明確指定兩個來源，在本 repo 根目錄執行：

```bash
python3 scripts/build_evo_upload.py \
  --lin-source /Users/wd-t160/LINS/git/skills/lin-skill/Lin-EVO \
  --miffy-source /Users/wd-t160/LINS/git/skills/Miffy-EVO \
  --output dist/claude-upload/Lin-EVO-Miffy-EVO-YYYYMMDD.zip
```

也支援原本的來源管理目錄參數：

```bash
python3 scripts/build_evo_upload.py --source /你的本機路徑/lin-skill --output dist/claude-upload/Lin-EVO-Miffy-EVO-YYYYMMDD.zip
```

有 `skill-sources.json` 時依其設定定位，沒有時才使用來源目錄下的 `Lin-EVO/`、`Miffy-EVO/`。明確的 `--lin-source`／`--miffy-source` 優先於管理目錄設定。缺來源直接回報，不從歷史包或其他機器路徑猜替代檔案。

打包器只讀來源，將入口轉為包內指南，保留工程師套件原檔，核對參考連結、逐檔一致及 ZIP 完整性。SOURCE.json 分別記錄兩個來源的路徑、來源檔案雜湊與可用的 Git commit；來源未受 Git 追蹤時其 commit 為 null，不冒用另一個 Skill 的版本。工程師版本讀實際 VERSION，不寫死。

既有同名包不覆蓋；這是 Claude Skill 包，不是客戶網站匯入 ZIP。使用整合包時停用重複的舊 Lin／Miffy 上傳包；若採分別上傳的兩個 Skill，維持各自啟用，不再疊加整合包。整體視覺 workflow 包另行啟用。

工程師提供新版時依 Miffy 規範人工更新實際來源，再重建相關包。打包通過不代表已在 Claude 實際上傳或完成 EVO 後台驗收；無本機或內網存取能力時需提供案件檔案，不能偽造檢查報告。

## Claude 網頁／App：專用上傳 ZIP

Claude 網頁／App 的 Customize → Skills → Upload a skill 使用專用包；不要上傳整個維護 repo，也不要將上方 install.py 分享包當成單一上傳 Skill。維護者在 repo 根目錄執行：

```bash
python3 scripts/build_claude_upload.py \
  --output dist/claude-upload/Visual-Solution-Workflow-日期.zip
```

檔名日期換成本次日期；同名輸出已存在時不覆蓋。Skill 名稱為 `Visual-Solution-Workflow`，產物只有一個同名根資料夾與入口 SKILL.md，僅附 workflow 的流程參考。Lin-EVO 與 GSAP 由使用者另外上傳／啟用，本包不重複內附；Eagle 與系統 CSS 也不打包。SOURCE.json 記錄 workflow commit、外部 Skill 依賴與各檔案雜湊。打包器檢查內部連結、ZIP 完整性，排除 Git、安裝器、案例與其他本機資料。

2026-10-14 上傳版由 `visual-solution-cloud` 更名為 `Visual-Solution-Workflow`；舊整合包與舊名 workflow-only 包均改用新的同名 ZIP。已獨立上傳 Lin-EVO／GSAP 的使用者不需要重複內附這些 Skill。

此包優先套用網頁／App 環境規則，不要求本機安裝、Git 更新、Chrome 或 Eagle 連線。使用者須提供案件檔案；未接入工具或無法存取內網時列缺口，不宣稱已在本機或正式後台驗證。上傳後啟用 Skill，另以本案需求測試；打包檢查不代表已通過 Claude 實際上傳／執行。來源更新後由維護者重新打包並重新上傳，不會自動追蹤本機 Git。
