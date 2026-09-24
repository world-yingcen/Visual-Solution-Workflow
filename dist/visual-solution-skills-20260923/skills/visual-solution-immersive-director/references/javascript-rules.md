# 整體視覺方案｜JavaScript 與動態初始化

靜態工程採以下入口；框架專案沿用既有路由與模組，記錄對應，不擅自重構。

## T10｜JavaScript 結構與初始化

- 沿用案件既有套件版本與載入方式；一般簡單功能可由原生 JavaScript 完成時，不額外加入大型套件。輪播統一依 T11 使用 Swiper。

- 首頁專用 JavaScript 統一放 `js/index.js`，內頁專用 JavaScript 統一放 `js/innerpage.js`；首頁載入 index.js，各內頁載入 innerpage.js，不把頁面程式散寫在 HTML，也不將首頁與內頁功能混入同一入口。
- Header／Footer 載入與全站共用互動仍集中於共用 JavaScript，沿用案件既有共用載入方式，不在 index.js 與 innerpage.js 各複製一份。既有 main.js 先盤點用途，不直接覆蓋或刪除；頁面專用功能依上述分工整理。
- 每段功能前用繁體中文註解清楚標示「控制哪個頁面／區塊、控制哪個元素、執行什麼功能」，例如 `// 首頁｜最新消息 .tpl-news：控制輪播與上一則／下一則按鈕`。innerpage.js 依內頁用途分段，並確認對應元素存在才執行。可調參數放各段開頭，註明用途、單位與原因。
- 文案、圖片與連結直接寫在 HTML，方便修改及後續套後台；JavaScript 負責互動與控制，不將產品、消息等內容整批放入 JS 陣列再產生畫面。data 屬性可放分類值、切換目標等必要控制資訊，實際內容仍放 HTML。Header／Footer 依 T13 載入共用 HTML。
- 每個元件從自己的 root 查找節點，支援多實例，不跨區塊抓控制項。DOM 就緒後初始化；若腳本較晚載入，也要能對現有 DOM 執行。
- 初始化前優先沿用既有程式或套件的狀態判斷，確保同一元件不重複初始化、事件不重複綁定；不強制使用 WeakSet／WeakMap，也不一律禁止以 data 屬性或 class 記錄狀態。先確認必要節點與套件，成功後才記為已初始化；失敗須清理本次部分註冊並保留重試能力，狀態標記不能與實際實例脫節。
- 事件去重，window／document 級監聽器只註冊一次。動態插入內容有需求才用 MutationObserver 掃描尚未初始化的 root，不預設全站持續重掃。
- resize、重新掛載與移除元件時，處理重複初始化、監聽器解除及套件實例生命週期；避免重複節點、累積位移與多次事件觸發。
- 禁止 eval、new Function、inline on*、javascript: URL 及未限縮範圍的全域 DOM 操作。一般外觀與互動狀態以 class 控制，樣式集中在 SCSS。
- 需要依實際內容或畫面即時計算的尺寸、位置，可由 JavaScript 設定 element.style，例如依內容計算展開高度；註明用途，尺寸或狀態改變時更新，結束使用時清理自身設定，避免留下過期值。不要用行內樣式取代一般 SCSS。
- Swiper 等套件自行產生的必要行內樣式正常保留，不任意清除；需要重建或移除元件時依套件生命週期處理，不把執行中產生的樣式抄回 HTML 原始檔。
- 預覽保留實際需要的 CSS／JS 載入，套件先於初始化程式。來源與版本沿用案件。
- 有 Node 時對修改的 JS 執行 `node --check`；工具缺少要記未驗證，不能當成通過。語法檢查後仍須實際操作與查 console。

## T11｜Swiper 與整體視覺動態

輪播沿用本案 Swiper 版本及內建控制，不重寫既有箭頭、分頁、拖曳與循環功能。CSS／JS 版本一致，套件先於初始化，覆寫樣式置於套件 CSS 之後。控制項限元件 root；依張數與顯示數設定 loop，單張或沒有控制項不報錯。observer 等設定依需求啟用，不預設全開；檢查實例、resize 與 console，不只查 script 標籤。

GSAP、ScrollTrigger、3D、WebGL、視差與釘選可依確認的設計使用，不套用簡單動態上限。依 [技術架構](technical-architecture.md) 管理場景及單一捲動責任；共用 HTML、圖片及字型尺寸穩定後必要時刷新量測，不靠重複初始化修正位置。

在頁面離開、重掛載或元件移除時清理自身事件、observer、RAF、計時器、timeline／ScrollTrigger 與 GPU 資源。保留套件必要的執行時 style，用實例自身 revert／dispose 清理，不整批清除其他元件的 style、aria 或 id；避免多個動畫搶同一 transform。減少動態仍保留完整資訊與操作。
