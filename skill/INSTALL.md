# 安裝整體視覺主 Skill

現行製作流程只有 `visual-solution-immersive-director` 一個主 Skill。`eagle` 與 `eagle-visual-solution-curator` 是團隊共用的資源庫工具，會一起安裝，但不是網站製作角色。

套件另附 8 個 `gsap-*` 技術 Skills：core、timeline、scrolltrigger、performance、plugins、utils、react、frameworks。安裝程式會一併安裝，主 Skill 按需讀取，不會每次全部載入，也不會安裝 GSAP JavaScript 套件。來源與使用界線見 [GSAP 技術 Skills](skills/visual-solution-immersive-director/references/gsap-skills.md)。只搬主 Skill 資料夾會缺少這些參考，請安裝整包。

安裝由使用者要求時執行。主 Skill 在每次開始或接續案件時會自動執行一次 `--update` 保持最新；其他時候不自動安裝依賴或修改權限。

把 repo clone 到本機固定資料夾（每台電腦各一份，不放雲端硬碟；GitHub 帳號需先被加為協作者），套件在 `skill/` 子資料夾，指令都在那裡執行。需要 Python 3.9 以上：

```bash
git clone https://github.com/world-yingcen/Visual-Solution-Workflow.git
cd Visual-Solution-Workflow/skill
python3 install.py --dry-run
python3 install.py
python3 install.py --status
```

預設安裝到 `~/.claude/skills`；Codex 可明確指定目標：

```bash
python3 install.py --target ~/.codex/skills
```

預設建立捷徑指向套件資料夾，改 repo 即生效，所以資料夾不要搬；Windows 無法建捷徑時自動改用複製。拿到 zip 而非 clone 的人加 `--copy`，複製安裝在來源更新後需重新執行。同名非本安裝器管理的資料夾會跳過，不自動覆蓋。完成後在對應執行端重新載入 Skill。

安裝器只處理這份套件明列的主 Skill、8 個 GSAP 技術支援與 2 個 Eagle 工具；即使 `skills/` 內另有資料夾，也不會順便安裝。Eagle Skill 的安裝不會另外安裝 Eagle 應用程式；團隊電腦既有的 Eagle 仍須在使用時保持開啟。

`--update` 會取得 repo 更新並同步安裝；主 Skill 每次開始或接續案件會自動執行一次，使用者也可自行執行。Codex 請使用 `python3 install.py --update --target ~/.codex/skills`，避免更新到預設的 Claude 技能目錄。若在受限案件工作區出現 `.git/FETCH_HEAD: Operation not permitted`，是該執行環境不能寫入案件外的來源庫；核對來源庫狀態後，取得執行環境的寫入核准再重跑，不要改檔案權限或重置 Git。沒有網路、不是 git clone 或本機分歧時，既有安裝不受影響。`--uninstall` 依安裝紀錄移除該工具管理的項目，執行前先核對 `--status`。`--case` 是舊版 Claude 案件權限設定相容功能，並非使用主 Skill 的必要步驟；只有明確要求該設定時才使用。

既有舊角色安裝不會自動刪除；若要清理，先核對安裝位置與來源，再另外處理。工程工具依案件實際需要準備，不要求每案固定安裝 Sass、Node、Eagle 或 VS Code。
