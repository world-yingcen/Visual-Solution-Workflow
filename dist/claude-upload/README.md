# Claude App 上傳包

## 目前版本：2026-10-22

請使用以下兩包；其他日期的檔案保留作歷史版本，不再作為最新安裝入口。

| 上傳包 | 維護來源 commit |
|---|---|
| [Lin-EVO＋Miffy-EVO](Lin-EVO-Miffy-EVO-20261022.zip) | lin-skill `b670bc2d6138eac88948546a6ce0b79ceab95a50` |
| [整體視覺流程](Visual-Solution-Workflow-20261022.zip) | Visual-Solution-Workflow `2009aeb1e92e04e77462c42c560b99e9f7251625` |

更新包含工作前 Git 檢查、換電腦前 commit／push、先讀交接再續作，以及已成功轉 EVO 後停止修改／推送原靜態 Git。整體視覺包沿用 Claude 提供 prompt、人工 ChatGPT 產圖與圖片處理的分工。工程師 evomni-html 1.1.0 套件保持原檔，未改寫。

在 Claude App 重新上傳並啟用新版，停用同名舊版及舊獨立 Lin／Miffy，避免重複規範；開新對話確認能讀取新版。**本機 Codex／Claude Code 安裝同步、Git push 與 ZIP 建立，不代表 Claude App 雲端已上傳或啟用。**

每包的 `SOURCE.json` 記錄來源 commit、建置時間與逐檔 SHA-256。這是 Skill 規範包，不是客戶網站匯入 ZIP。打包方式見 [安裝與維護說明](../../skill/INSTALL.md)。

## ZIP SHA-256

- Lin／Miffy：`7f1cc5c0adac96aed96371077cbd0288b6d8e5ff348d187edc9418bcc5656a0a`
- 整體視覺：`6f6d21fb363662489394bc8fc6da63f6df3e4550692edefb1fd775bb2ceba19f`
