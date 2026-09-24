# 整體視覺方案 Skills 分享包

這份套件只含工作流程、技術參考與安裝程式，不含客戶案件、圖片、字型、案例資料庫或憑證。

## 內容

- `visual-solution-immersive-director`：唯一主入口。
- 8 個 `gsap-*` Skill：主 Skill 按需求讀取的技術支援，不是額外角色。
- `eagle`、`eagle-visual-solution-curator`：團隊共用的資源庫工具，會一起安裝。

## 安裝

把這個套件 clone 到本機固定資料夾（每台電腦各一份，不放雲端硬碟），在資料夾內開啟終端機：

```bash
python3 install.py --dry-run
python3 install.py
python3 install.py --status
```

預設建立捷徑指向這個資料夾，Windows 無法建捷徑時自動改用複製；拿到 zip 的人改加 `--copy`。Codex 使用者在指令後加 `--target ~/.codex/skills`。主 Skill 每次開始或接續案件會自動執行一次 `python3 install.py --update` 保持最新。Skill 安裝不會另裝 Eagle 應用程式；使用 Eagle 功能時，接收者電腦上的 Eagle 需保持開啟。詳細界線見 `INSTALL.md`。

## 使用

重新載入對應的 AI 工具後，可說：「使用 `$visual-solution-immersive-director` 盤點這個案件，先判斷模式與目前階段。」主 Skill 會依階段讀取 references，不會一次載入所有文件。

開案準備、五個確認點、回饋方式與疑難排解見 `使用教學.md`；圖文版 `使用教學.html` 用瀏覽器開啟即可。

## 驗證邊界

分享包保留來源 Skill 的規則與已知驗證限制。案例經驗以文字摘要隨附，但客戶案例與素材不在包內；沒有實際案例畫面時，不得宣稱已重新驗證案例品質。
