# 安裝整體視覺主 Skill

現行製作流程只有 `visual-solution-immersive-director` 一個主 Skill。`eagle` 與 `eagle-visual-solution-curator` 是團隊共用的資源庫工具，會一起安裝，但不是網站製作角色。

套件另附 8 個 `gsap-*` 技術 Skills：core、timeline、scrolltrigger、performance、plugins、utils、react、frameworks。安裝程式會一併安裝，主 Skill 按需讀取，不會每次全部載入，也不會安裝 GSAP JavaScript 套件。來源與使用界線見 [GSAP 技術 Skills](skills/visual-solution-immersive-director/references/gsap-skills.md)。只搬主 Skill 資料夾會缺少這些參考，請安裝整包。

只有使用者要求安裝或更新時才執行。日常開案不自動更新、安裝依賴或修改權限。

在此套件目錄使用 Python 3.9 以上：

```bash
python3 install.py --dry-run --copy
python3 install.py --copy
python3 install.py --status
```

預設安裝到 `~/.claude/skills`；Codex 可明確指定目標：

```bash
python3 install.py --target ~/.codex/skills
```

`--copy` 使用複製；預設可用時建立捷徑。複製安裝在來源更新後需重新執行。同名非本安裝器管理的資料夾會跳過，不自動覆蓋。完成後在對應執行端重新載入 Skill。

安裝器只處理這份套件明列的主 Skill、8 個 GSAP 技術支援與 2 個 Eagle 工具；即使 `skills/` 內另有資料夾，也不會順便安裝。Eagle Skill 的安裝不會另外安裝 Eagle 應用程式；團隊電腦既有的 Eagle 仍須在使用時保持開啟。

`--update` 會取得 repo 更新並同步安裝，僅在明確要求更新時使用。`--uninstall` 依安裝紀錄移除該工具管理的項目，執行前先核對 `--status`。`--case` 是舊版 Claude 案件權限設定相容功能，並非使用主 Skill 的必要步驟；只有明確要求該設定時才使用。

既有舊角色安裝不會自動刪除；若要清理，先核對安裝位置與來源，再另外處理。工程工具依案件實際需要準備，不要求每案固定安裝 Sass、Node、Eagle 或 VS Code。
