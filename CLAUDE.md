# 整體視覺方案套件

先讀 [skill/AGENTS.md](skill/AGENTS.md)。這個 repo 只放 Skill 套件（`skill/`），同事直接 clone 使用；案例在維護者本機的 `Visual-Solution-Workflow-case/cases/`，不在這裡。使用者要求整理／修改 Skill 時就維護 `skill/`，不啟動客戶網站流程。

使用者明確要執行案件時，讀 [整體視覺主 Skill](skill/skills/visual-solution-immersive-director/SKILL.md)，依案件實際進度與確認紀錄接續。由當前任務整合設計與製作，不預設五角色或跨工具派工；Codex 與產圖工具依開案時記錄的授權沿用，不能以角色名稱代替真實檢查。

安裝依 [skill/INSTALL.md](skill/INSTALL.md) 處理。在套件資料夾維護 Skill 時不自動更新、修改權限或安裝 Skills；執行案件時由主 Skill 在每次開始或接續時自動執行一次 `python3 install.py --update` 保持最新。查看狀態可用 `python3 skill/install.py --status`。本套件不預設已安裝，也不修改原高效流程。
