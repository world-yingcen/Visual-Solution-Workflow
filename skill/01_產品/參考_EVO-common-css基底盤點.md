# EVO-common-css 本機基底盤點

日期：2026-09-08。唯讀檢查，未修改來源或連線驗證遠端最新版本。

來源：`/Users/wd-t160/LINS/git/EVO-common-css`，本機 HEAD：`dbd1d5ed1cc5b5a7d580a10ddf7e8af8e7ef4e9f`。Git 工作區僅列 `.DS_Store` 修改；README.md 不存在。

```text
06-切版/
├── index.html
├── assets/page-composer-state.json
├── image/.gitkeep
├── js/main.js
└── scss/
    ├── _common.scss
    ├── _header.scss
    ├── _footer.scss
    ├── _index.scss
    └── evomni-root.scss
```

`evomni-root.scss` 依序使用 `@import "common"`、`header`、`footer`、`index`。沿用現況，不在此步驟改成另一套拆檔或匯入方式。

目前 index.html、main.js、page-composer-state.json、_footer.scss、_index.scss 為 0 bytes。Common 與 Header 有內容。此次列檔未見 package.json、Sass 編譯設定或 evomni-root.css，不能宣稱 clone 後即可預覽；初始化仍需填入內容、配置 compiler 並確認 CSS 載入。

已確認：使用完整來源中的 06-切版 子目錄，避免 06-切版/06-切版 重複包覆。每次開案仍重新讀取實際 clone 版本，本機快照不當成所有未來版本的固定結構。內頁需求超出基底時才補必要檔案，未確認逐頁拆 SCSS 方案。
