# 整體視覺方案 Skills 分享包

這份套件只含工作流程、技術參考與安裝程式，不含客戶案件、圖片、字型、案例資料庫或憑證。

## 內容

- `visual-solution-immersive-director`：唯一主入口。
- 8 個 `gsap-*` Skill：主 Skill 按需求讀取的技術支援，不是額外角色。
- `eagle`、`eagle-visual-solution-curator`：團隊共用的資源庫工具，會一起安裝。

## 安裝

先解壓縮，在此資料夾開啟終端機：

```bash
python3 install.py --dry-run --copy
python3 install.py --copy
python3 install.py --status
```

Codex 使用者在三個指令後加 `--target ~/.codex/skills`。Skill 安裝不會另裝 Eagle 應用程式；使用 Eagle 功能時，接收者電腦上的 Eagle 需保持開啟。詳細界線與更新方式見 `INSTALL.md`。

## 使用

重新載入對應的 AI 工具後，可說：「使用 `$visual-solution-immersive-director` 盤點這個案件，先判斷模式與目前階段。」主 Skill 會依階段讀取 references，不會一次載入所有文件。

## 驗證邊界

分享包保留來源 Skill 的規則與已知驗證限制。案例經驗以文字摘要隨附，但客戶案例與素材不在包內；沒有實際案例畫面時，不得宣稱已重新驗證案例品質。
