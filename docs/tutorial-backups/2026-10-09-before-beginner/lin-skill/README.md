# LIN 網頁切版與校稿 Skill

分享給設計師與前端實作者的獨立套件，Skill 名稱為 `lin-frontend`。可用於 Claude Code 與 Codex 的 Skill 資料夾。

教學更新：2026-10-09。第一次使用依序看安裝、叫用範例與下方「靜態切版到 EVO」；已安裝者可直接看實際製作與交付方式。

## 內容與使用範圍

整理自整體視覺方案套件中的 LIN 工程條文：HTML／SCSS 命名、Common、container、RWD、JavaScript 初始化、Swiper、共用 Header／Footer、Nav 與實作校稿。

本包不含客戶案件、圖片、字型、Common CSS 原始碼或網站基底；也不含 Eagle、GSAP 技術 Skills 與整體視覺提案流程。不依賴原維護者電腦上的檔案，不固定桌機尺寸。需搭配接收者的實際工程與設計稿使用。

要轉 EVO 的案件另需工程師提供的 evomni-page-composer 範本資料，使用接收者自己的套件位置；這份 LIN 教學不要求改走後台直接產頁流程。

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


## 靜態切版到 EVO：設計師實際怎麼用

流程是：**設計師與 AI 完成靜態網站及互動 → 客戶校稿確認 → 工程師轉 EVO 後台 → 後台編輯與前台整合驗證。**

整體視覺案件仍先做 2560×1280 桌機，RWD 另行提出；獨立 lin-frontend 依案件約定尺寸與 RWD 製作。下面是共同的工程交付方式，不改變各自的設計流程。

### 開始前，給 AI 這些資訊

提供案件資料夾、設計稿／已確認頁面、素材與文案，以及工程師提供的 evomni-page-composer 套件位置。位置填你電腦上實際的路徑，不照抄別人的使用者名稱。這個工程師套件是範本與平台契約的查詢來源，沒有附在本 Workflow／LIN 分享包內；找不到時請向工程師取得，AI 會標示尚未核對的部分。

```text
這個案件先完成靜態網站，客戶確認後交工程師轉 EVO。
案件資料夾：填本案路徑
設計稿與素材：填檔案位置或連結
工程師套件：填 evomni-page-composer 的本機位置
本輪製作範圍：填頁面、尺寸與 RWD 範圍

請先讀現有工程與進度，查工程師的範本資料再切版。
共用與單頁 CSS／JS 分開，每頁只引用自己需要的資源。
請主動判斷客戶可編輯項目；不確定用途或會影響設計時再問我。
完成完整可預覽的網站，交付時整理頁面對照表。
```

先用本教學前面的指令叫用對應 Skill，再貼這段即可。續作只需補上本輪範圍，已確認的資料不用重填。

### 哪些事交給 AI 判斷

| 遇到的需求 | AI 要做什麼 | 你需要做什麼 |
|---|---|---|
| 選單、FAQ、麵包屑等平台元件 | 查範本規格，保留必要結構，再配合本案外觀 | 確認設計與操作 |
| 自製品牌區塊 | 使用 designer-tpl-* 命名，完整做出設計與效果 | 確認構圖與效果 |
| 消息、產品、證書、團隊、輪播圖片 | 判斷內容來源與逐筆編輯需求，查平台契約 | 用途不明時回答是否需自行增刪 |
| 平台資料或文件不足 | 記錄具體缺口交工程師確認，先完成可做的靜態部分 | 提供已知資料即可，不必判斷 data 屬性 |

自製範例是 `designer-tpl-about`；平台 FAQ 仍保留 `tpl-faq001` 等原名。既有案件不會自動整站改名。你不用先背範本清單，AI 會讀工程師套件；查到規格不等於已完成 EVO 轉檔。

### CSS 在切版時就分好

以下是新案示意，既有案件沿用自己的位置與編譯工具。CSS 由 SCSS 編譯產生，不手動維護兩份相同樣式。

```text
網站/
├─ index.html
├─ about.html
├─ contact.html
├─ scss/
│  ├─ _common.scss             全站變數、字體、容器、按鈕
│  ├─ _header.scss             共用頁首
│  ├─ _footer.scss             共用頁尾
│  ├─ _innerpage-default.scss  內頁共用 Hero、CTA
│  ├─ evomni-root.scss         只匯入共用樣式
│  ├─ index.scss               首頁專用
│  ├─ about.scss               關於我們專用
│  └─ contact.scss             聯絡我們專用
├─ css/                       編譯輸出
│  ├─ evomni-root.css
│  ├─ index.css
│  ├─ about.css
│  └─ contact.css
└─ js/
   ├─ header.js                選單、漢堡、語系
   ├─ footer.js                頁尾、回頂部、全站初始化
   ├─ index.js                 首頁專屬互動
   └─ about.js                 關於我們專屬互動
```

例如 `about.html` 的樣式引用：

```html
<link rel="stylesheet" href="css/evomni-root.css">
<link rel="stylesheet" href="css/about.css">
```

若用到 Swiper 等套件，另載入必要套件 CSS，順序依本案確認。關於我們不能靠載入 contact.css 才正常。兩頁共用的 Hero 放共用檔，只有關於我們使用的沿革放 about.scss；合理的單頁差異可以覆寫，但 AI 要檢查實際權重。

工程師轉 EVO 時再將同一份來源對應到正式站的全站／單頁資源。既有站可能有不同輸出方式，例如 evo266200 正式 root 還需保留 index；不能照新案示意直接刪掉舊站的引用。

### JS 依功能分工

`header.js` 管選單、漢堡、語系；`footer.js` 管頁尾、回頂部與全站初始化。需要全站 Lenis 時，在 footer.js 建立一次；AOS 全站初始化也集中處理。Lenis 依設計需要啟用，不是每站必加。

首頁動畫放 index.js，關於我們動畫放 about.js。每頁只引用共用、本頁及必要套件；沒有專屬互動就不用建立空 JS。AI 負責等待套件、DOM 與共用 HTML 就緒，並避免重複啟動；放在頁尾不代表非同步內容已經載完。

靜態預覽需有實際可用的套件與初始化。轉 EVO 後，data-vendor 是載入宣告，不會自動啟動輪播；套件版本與正式接入方式交工程師依目標站台確認。畫布預覽設定與前台初始化也分開核對。

### 內頁 HTML 與客戶可編輯內容

AI 會將內頁識別放在 main 內第一層，避免轉檔後遺失：

```html
<main id="main-content" class="main-content">
  <div class="inner-page about-page">
    <section class="designer-tpl-about">
      <h1 class="main-title">關於我們</h1>
      <p class="description">本案已確認的公司介紹。</p>
    </section>
  </div>
</main>
```

這只是主要內容示例；交付的靜態網站仍包含完整 head、頁首、頁尾和資源。樣式可寫 `.about-page .main-title`，不能寫 `.about-page .main-content`，因為 main-content 在外層。

客戶會更新的文字、圖片與清單保留在可編輯內容中。AI 主動判斷增刪、排序、換圖需求；資料庫產品、平台 FAQ 與一般圖片清單各用適合的契約，不一律套同一種標記。第一筆作樣板時，各筆結構一致。

例如「100 年經驗」改成「120 年經驗」，動畫應跟著跑到 120。AI 要測試改字、換圖及項目數改變後的效果；暫時的拆字標籤、數字動畫與輪播複製節點不能存回原始內容。後台存檔的接入由工程師驗證，動畫失敗時內容仍須看得到。

### 首次製作要包含什麼

首次就一起完成共用 Header／Footer、回頂部、Cookie 提示與有內容的隱私權政策頁。「隱私權政策」文字須連到本案實際頁面；缺正式政策文案時完成草稿並列待確認項目，不把草稿當客戶已核准。

Cookie 外觀與文字、選單、FAQ、麵包屑、跑馬燈依 Skill 的指定參考。輪播用 Swiper，區塊淡入淡出用 AOS，複雜動態依已確認設計使用 GSAP；固定圖片效果優先處理於素材。Footer 版權列沿用規範的 Designed by 米洛科技有限公司，不加客戶 © 或年份。

### 校稿完成後怎麼交工程師

你可以直接說：

```text
請整理這版的工程師交付資料。
依實際檔案列出每頁 HTML、SCSS／CSS、JS、共用依賴、
套件版本、動畫功能與客戶可編輯項目。
檢查資源缺檔、路徑、單頁獨立預覽及本輪範圍內的 RWD。
保留完整靜態預覽，列出仍需工程師接入或確認的地方。
```

AI 會填好這類對照表，你不用手填。下面只是示例，不代表本案已經完成：

| 頁面 | HTML | 專屬 SCSS → CSS | 專屬 JS | 共用依賴 | 套件 | 互動效果 | 客戶可編輯 |
|---|---|---|---|---|---|---|---|
| 關於我們 | about.html | about.scss → about.css | about.js | root CSS、header/footer HTML 與 JS | Swiper／實際版本 | 數字滾動、證書輪播；附初始化函式 | 數字、證書圖片與順序 |
| 聯絡我們 | contact.html | contact.scss → contact.css | 無（本例無專屬互動） | 同上 | 無額外套件 | 電話／Email 連結 | 聯絡資訊 |

表下附啟動與編譯方式、套件與程式順序、初始化時機、檢查結果及待確認項目。表單沒有後端時明示待串接，不以假的成功訊息當完成。

### 四種進度分開看

| 狀態 | 代表什麼 |
|---|---|
| 靜態預覽驗證 | 已在瀏覽器測過指定頁面、動畫及授權尺寸 |
| 客戶確認 | 客戶確認了特定版本與範圍 |
| 工程師轉檔 | 工程師已處理 EVO 輸出與後台接入 |
| 後台／前台整合驗證 | 已實測編輯、儲存、發布後內容與效果 |

目前這輪完成的是 Skill 與教學文件整理，尚無本輪新規則的實際案件轉檔驗證。未來交付時仍需依每案實際結果填寫。

### 遇到問題可以這樣說

- 「關於我們拿掉其他頁 CSS 就跑版，請找出藏錯位置的共用樣式。」
- 「客戶改數字後，動畫還是舊值，請讓動畫讀取最新內容。」
- 「輪播圖片要讓客戶自行增刪，請查工程師套件的編輯契約。」
- 「只修這個區塊，保留其他頁與已確認動態。」
- 「套件規格與工程師指南不同，請列出差異及待確認項目。」


## 維護

規則細節：[HTML／CSS](lin-frontend/references/html-css-rules.md)、[JavaScript](lin-frontend/references/javascript-rules.md)、[EVO 查核與交付](lin-frontend/references/evo-preflight.md)、[校稿檢查](lin-frontend/references/implementation-review.md)、[Cookie 與政策頁](lin-frontend/references/evo-cookie-reference.md)。

有效來源為本資料夾的 `lin-frontend/`。本包的整理不會修改或安裝原本整體視覺套件；後續更新需重新提供分享包。規範的外觀與行為仍須在接收者工程中實看驗證。
