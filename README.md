# 整體視覺方案工作流程

以品牌、內容與使用者任務為起點，整合專屬構圖、影像、排版與互動，交付完整的整體視覺網站。採單一主 Skill，不預設五角色流程。

## 目錄

這個 repo 只放 Skill 套件，同事直接 clone 使用；案例不在這裡。

- `skill/`：Skill 套件——主 Skill、8 個 GSAP 技術 Skills、2 個 Eagle 工具、安裝程式與測試。文件：[使用教學](skill/使用教學.md)（[圖文版](skill/使用教學.html)）、[安裝說明](skill/INSTALL.md)、[工作規則](skill/AGENTS.md)、[轉版狀態](skill/轉版狀態.md)。`skill/01_產品/` 是 Common CSS、系統功能與內頁版型的共用技術參考，不進分享包。
- `.claude-plugin/marketplace.json`、`skill/.claude-plugin/plugin.json`：讓 Claude Code 以 Plugin 安裝 `skill/`（`/plugin marketplace add world-yingcen/Visual-Solution-Workflow`）。Codex 仍用 install.py。
- `scripts/build_share_package.py`：從 `skill/` 打包 zip 到 `dist/`（給沒有 git 的人）。
- `lin-skill/`：另外整理的 [LIN 網頁切版與校稿獨立分享包](lin-skill/README.md)，供一般網站切版使用；不加入原套件的安裝清單。
- 案例（`projects/`、`final/`、`最終版彙整/`、`template-library/` 資料庫）在維護者本機的 `Visual-Solution-Workflow-case/cases/`，不進這個 repo。

## 工作入口

- [整體視覺網站設計與製作](skill/skills/visual-solution-immersive-director/SKILL.md)：以品牌方向、核心片段試做、素材製作與瀏覽器修正循環完成整體視覺網站。目前以 MASSIF／Elysian／Noctave／Axisform 類「整體視覺」為核心範圍；品牌賦能需先完成品牌母題與專屬資產。尚待真實案件端到端驗證。

## 設計與製作

先整理案件 PRD，再整合品牌、參考用途與 Design Brief，確認方向後進入施工。參考可以是忠實重建、指定特徵轉譯或原創方向的品質參考，不能由 AI 自行混用。

主 Skill 統整具體構圖、圖片條件與互動狀態，先驗證核心片段，再依整頁場景表延伸全部內容。依本案約定尺寸及階段驗收；使用者指定先完成桌機時，先完成指定尺寸。整頁檢查依 [完整度規則](skill/skills/visual-solution-immersive-director/references/full-page-completeness.md) 執行。

套件早期由其他流程轉版，歷史來源不代表沿用其製作規則。資料庫保留的高效案例是歷史紀錄，不是本方案母版。新版規則尚待下一件完整案件驗證。
