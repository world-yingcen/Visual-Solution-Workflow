# 案件推送到公司 Git

依公司文件「內部 Git 專案空間使用說明（放置 AI HTML）」（posthub 文件 2335，2026-09-21）整理成 CLI 流程，由本 Skill 在使用者要求「推到 git」「備份到 git」「同步 git」時直接執行，不要求使用者改用 VSCode 按鈕操作。伺服器是公司內網 `http://192.168.168.134/client-html-demo`，需在公司網路或 VPN 內；專案清單同一網址可查。

## 界線

- 只在使用者明確要求時執行，不在確認點以外主動推送。每次推送前列出目標專案、分支與將提交的檔案摘要，執行後回報結果。
- 帳號是公司信箱 @ 前的英文，密碼由工程師開立。Skill 不索取、不輸入、不儲存密碼；第一次推送若出現帳密提示，請使用者在自己的終端機執行一次 `git push`，讓憑證管理員記住後再由 Skill 接手。
- 不用 `--force`，不刪遠端分支或專案，不改寫別人的 commit。衝突無法判斷時停下來讓使用者選。
- 推送對象是完整網站資料夾（首頁、內頁、css、js、assets 同一層），不是整個案件資料夾；客供原件、PSD、影片原檔與案件文件不推，除非使用者指定。首次推送時確認資料夾與專案英文 ID，記入進度檔。
- 案件資料夾在 Google 雲端硬碟時，`.git` 也會被同步：推送前後不要在另一台電腦同時操作；發現 `.git` 損壞或狀態異常先停下回報，不自行重建。

## 前置檢查（每次執行前）

```bash
git --version
git config --global user.name
git config --global user.email
git config --global credential.helper
```

- 沒有 git：Mac 請使用者執行 `xcode-select --install`；Windows 到官網下載安裝，一路使用預設。需要管理者密碼時請使用者找安志或阿久，Skill 不代為輸入。
- `user.name` 統一為「暱稱(全名)」或「全名」，例如 `LIN(林盈岑)`、`劉淑慧`；`user.email` 是公司信箱 `@world-group.com.tw`。缺少或格式不符時，請使用者提供後由 Skill 設定：

```bash
git config --global user.name "暱稱(全名)"
git config --global user.email "帳號@world-group.com.tw"
```

- 憑證管理員為空時設定（Mac `osxkeychain`，Windows `manager`），並告知使用者第一次推送要自己輸入一次帳密。

## 情況 A：新網頁建立新專案

在網站資料夾執行。專案英文 ID 由使用者指定（英文、數字、連字號），`project.description` 填效率雲上的客戶名稱。

```bash
git init -b main                 # 舊版 git：git init 後 git branch -M main
printf '.DS_Store\nThumbs.db\n' > .gitignore
git add -A
git commit -m "首頁桌機版 v1"      # 白話寫這個版本是什麼
git remote add origin http://192.168.168.134/client-html-demo/專案英文ID.git
git push -u origin main -o project.create -o project.visibility=public -o "project.description=效率雲客戶名稱"
```

推送成功後主機會自動建立專案；把專案網址、推送的資料夾與 commit 記入進度檔。已有 `.git` 的資料夾不重新 init，先看 `git status` 與 `git remote -v`。

## 情況 B：下載既有專案

```bash
git clone http://192.168.168.134/client-html-demo/專案名稱.git 目標資料夾
```

需要帳密時由使用者輸入。下載後先讀 README 與進度檔再接續。

## 情況 C：修改後同步上傳

對應 VSCode 的「準備存檔 → 提交 → 同步變更」：

```bash
git status
git add -A                                   # 或只加使用者指定的檔案
git commit -m "修改說明，例如：新增活動頁首 Banner"
git pull origin main                         # 先抓同事的最新版
git push origin main
```

`git pull` 出現衝突時進入情況 D；沒有衝突就直接推送並回報。

## 情況 D：衝突

兩個人改到同一個檔案的同一行時，`git pull` 會停下並標記衝突檔。

1. `git status` 列出衝突檔案，逐檔展示衝突區塊，說明「目前的變更＝自己這台電腦的內容」「傳入的變更＝同事上傳的內容」。
2. 請使用者逐檔選擇：保留自己、保留同事、兩者皆保留。Skill 依選擇修改檔案，不自行決定；使用者要改在 VSCode 用按鈕處理時，停下等他完成。
3. 解決後：

```bash
git add 衝突檔案
git commit -m "解決衝突"
git push origin main
```

## 回報與紀錄

- 每次執行後回報：專案網址、分支、commit 訊息、推送的檔案數、刻意未推的項目、是否有衝突與如何解決。
- 進度檔記錄：Git 專案 ID 與網址、推送的資料夾、最近一次推送的 commit 與日期。
- 推送成功不等於客戶定稿或交付完成；交付與後台交接仍依使用者指示。
