# 整體視覺方案｜維護 repo

- `skill/`：Skill 套件本體，工作規則見 [skill/AGENTS.md](skill/AGENTS.md)；同事 clone 這個 repo 後在 `skill/` 內安裝。
- 案例（`projects/`、`final/`、`最終版彙整/`、`template-library/`）在維護者本機的 `Visual-Solution-Workflow-case/cases/`，不在這個 repo；供查閱與案例維護，不構成製作規則。
- `scripts/build_share_package.py`：打包套件成 zip；`dist/` 是輸出。

修改流程文件不自動啟動客戶案件、不安裝工具、不推送或部署。
