# LIN 網頁切版與校稿 Skill

分享給設計師與前端實作者的獨立套件，Skill 名稱為 `lin-frontend`。可用於 Claude Code 與 Codex 的 Skill 資料夾。

## 內容與使用範圍

整理自整體視覺方案套件中的 LIN 工程條文：HTML／SCSS 命名、Common、container、RWD、JavaScript 初始化、Swiper、共用 Header／Footer、Nav 與實作校稿。

本包不含客戶案件、圖片、字型、Common CSS 原始碼或網站基底；也不含 Eagle、GSAP 技術 Skills 與整體視覺提案流程。不依賴原維護者電腦上的檔案，不固定桌機尺寸。需搭配接收者的實際工程與設計稿使用。

原規範的核心切版條文與範例保留，獨立版調整了驗收尺寸／RWD 範圍、外部文件連結及公司專用條文的適用說明。它是 LIN 工程規範獨立版，不是整體視覺主 Skill 的替代入口。未進行真實客戶案件端到端驗證。

## 安裝

1. 解壓縮分享包，開啟解壓後的資料夾。
2. 在此資料夾開啟終端機（需 Python 3），先試跑再安裝。

Codex：

```bash
python3 install.py --tool codex --dry-run
python3 install.py --tool codex
```

Claude Code：

```bash
python3 install.py --tool claude --dry-run
python3 install.py --tool claude
```

Windows 若 `python3` 找不到，改用 `py -3`。安裝完成後重新開啟對應 AI 工具。

安裝程式只複製 `lin-frontend/` 到所選工具的 Skills 資料夾，不改全域設定、不裝套件、不覆蓋同名檔案。若同名 Skill 已存在，先核對及移走舊版，再安裝；沒有自動更新或自動移除功能。

也可手動複製整個 `lin-frontend/` 到 `~/.codex/skills/` 或 `~/.claude/skills/`；Windows 對應使用者家目錄下的 `.codex/skills/` 或 `.claude/skills/`。不要只複製 SKILL.md，references 也要一起帶入。

## 叫用範例

Codex：

```text
使用 $lin-frontend，依這份 Figma／設計稿完成頁面。先讀現有 Common、元件與工程，沿用既有架構並完成切版與視覺校稿。
```

Claude Code：

```text
使用 lin-frontend，檢查這個頁面的 HTML、SCSS 與 JavaScript，直接修正違反 LIN 規範及影響版面、操作的問題。
```

局部修改可補：「本輪只調整產品區，不重構其他區塊，保留既有 RWD。」尺寸、RWD 與平台限制有指定時直接附上。

## 維護

有效來源為本資料夾的 `lin-frontend/`。本包的整理不會修改或安裝原本整體視覺套件；後續更新需重新提供分享包。規範的外觀與行為仍須在接收者工程中實看驗證。
