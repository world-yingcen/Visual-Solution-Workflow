# GSAP 技術 Skills｜按需使用

先依本案確認的分鏡決定動態目的、起訖與閱讀節奏，再讀需要的技術 Skill；不要每次載入全部，也不因範例而新增效果、改用框架或擴大 RWD 範圍。這些是技術參考，不是額外角色或多代理流程。

| 實際需求 | 讀取 |
| --- | --- |
| GSAP 基本動畫、easing、matchMedia、減少動態 | [gsap-core](../../gsap-core/SKILL.md) |
| 多段動畫排序、交疊、連續轉場 | [gsap-timeline](../../gsap-timeline/SKILL.md) |
| 捲動連動、pin、scrub、觸發位置 | [gsap-scrolltrigger](../../gsap-scrolltrigger/SKILL.md) |
| 動態效能設計、卡頓排查與優化 | [gsap-performance](../../gsap-performance/SKILL.md) |
| 確實需要額外 GSAP plugin | [gsap-plugins](../../gsap-plugins/SKILL.md) |
| 數值映射、限制範圍等工具函式 | [gsap-utils](../../gsap-utils/SKILL.md) |
| 既有專案為 React／Next.js | [gsap-react](../../gsap-react/SKILL.md) |
| 既有專案為 Vue／Nuxt／Svelte 等 | [gsap-frameworks](../../gsap-frameworks/SKILL.md) |

沿用案件 GSAP 版本、共用初始化、銷毀與捲動系統。範例不是直接覆蓋 LIN 結構的模板；涉及版本差異時再查相應官方文件。Skill 的安裝不等於安裝 GSAP JavaScript 套件，也不授權更新案件依賴。

## 隨附來源與限制

- 2026-09-20 從使用者本機已安裝的 8 個 `gsap-*` Skill 複製，保留原文、原名及 `license: MIT` 宣告；來源自述為 Official GSAP skill。本次未查證上游版本或是否最新。
- 隨附檔案為各自的 `SKILL.md`；來源沒有其他資源。`gsap-frameworks` 提到的 `examples/vue/`、`examples/nuxt/` 並未隨來源提供，不可宣稱這些可執行範例已內附。
- 所有上述連結指向本套件的兄弟 Skill，不依賴原使用者的電腦路徑或高效方案專案。請使用根目錄安裝程式安裝整包，不只單獨搬主 Skill。
- 若安裝器跳過既有同名 Skill，先核對來源與版本；不要自行覆蓋。需要替換時另取得使用者授權。
