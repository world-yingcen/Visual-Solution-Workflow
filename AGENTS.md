# 整體視覺方案｜維護 repo

- `skill/`：Skill 套件本體，工作規則見 [skill/AGENTS.md](skill/AGENTS.md)；同事 clone 的 repo 就是這一夾的內容。
- `cases/`：案例（`projects/`、`final/`、`最終版彙整/`、`template-library/`），供查閱與案例維護，不構成製作規則。
- `scripts/build_share_package.py`：打包或同步套件；`dist/` 是輸出。

修改流程文件不自動啟動客戶案件、不安裝工具、不推送或部署。
