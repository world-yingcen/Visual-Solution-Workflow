# Visual QA Standard

## Evidence Before Scores

Identify the build/commit or revision, route, browser, viewport and date. The default desktop gate is 2560×1280 CSS pixels. For each criterion record observed behavior, evidence path or reproducible steps, defect and verified/not-verified status. Capture composition at initial, middle and exit states; operate scroll forward/backward and the actual controls. Screenshots alone cannot pass motion quality.

Use browser performance measurement for numeric FPS or latency claims; report measurement conditions. Visual observation alone may describe stutter but cannot establish a numeric frame-rate guarantee. Check console and failed required resources, reload, reduced motion and relevant fallback states at 2560×1280. Do not add Tablet／Mobile／responsive QA unless the user has explicitly opened that later scope.

Distinguish implementation checks, AI visual assessment and user approval. Scores are provisional design judgments, not objective measurement. If a required category was not observed, mark it unverified and do not publish a passing total. Never claim independent review for self-review.

For a slice, assess only its promised scope. It cannot pass full-page content or site-wide consistency. Temporary key visuals cannot pass final asset fidelity. Fix blocking defects with `refinement-loop.md` and retest the same states plus affected adjacent transitions before changing scores.

Provide the user with an operable preview and a short list of remaining perceptual decisions at the approval gate. A validator/build success is not visual acceptance.

## Full-page gate

首次交付及整頁延伸依 [完成度基準](quality-baseline.md) 比較 Hero、一般內容段及 CTA 的素材、排版與閱讀節奏。實看後先修目前最弱的幾處，再提交使用者；已有功能但仍呈現暫代素材或未完成構圖時，明列該範圍，不把「可運作」當成視覺完成。

對照全頁場景表從 Banner 操作到 Footer，核對每段進入、閱讀、離開及相鄰交接是否落實。檢查重點轉場是否有內容目的、輕量銜接是否引導視線、安靜段是否真的適合閱讀，以及強動態之間是否有穩定停留。只有 Banner 有動態、其餘未完成規劃，或所有段落重複強效果而阻礙閱讀，都列為整頁節奏缺陷；不能用 Hero 分數抵銷。具理由的靜態段不扣分，hover／按鈕微動也不能替代已承諾的跨區塊轉場。

交付使用者前，先自行修正能從需求與畫面確認的缺陷：人物拆層不自然、材質不一致、裝飾遮擋、後半頁構圖未完成及非預期空白。使用者判斷方向與取捨，不承擔逐段找 bug 的工作。每次修改轉場或高度，至少重看本段與前後交接的正向、反向狀態；先讀取實際 CSS viewport 與縮放，不能把設定視窗尺寸視為尺寸驗證。

For a complete homepage, apply [整頁完整度](full-page-completeness.md) at 2560×1280, including the lower sections and footer. Record content coverage, asset framing, reading hierarchy, conversion actions and both scroll directions. A strong hero or high average score cannot compensate for an unfinished lower page. Desktop-only delivery must not be reported as responsive acceptance.

## Desktop Homepage Score — 100 points

### 1. Motion / Scroll Quality — 30
Judge:
- scroll feel,
- timing and easing,
- camera-like continuity,
- transitions,
- pinned behavior,
- zoom/scale progression,
- absence of stutter, drag, or forced waiting.

Hard gate: >=25/30.

### 2. Hero First Impression — 20
Judge:
- memorability,
- immediate world-building,
- brand presence,
- composition,
- invitation to continue.

Hard gate: >=16/20.

### 3. Visual Cohesion — 20
Judge:
- one coherent world,
- consistent typography/image/material/UI language,
- no quality cliffs between sections,
- brand assets integrated rather than pasted in.

Hard gate: >=16/20.

### 4. Peaks and Reading Rhythm — 15
Judge:
- clear wow moments,
- breathing room,
- contrast between high/low intensity,
- reading comfort,
- progression across the full page,
- presence of at least one brand-specific memorable moment where appropriate.

### 5. Information Clarity — 10
Judge:
- brand/product/service understanding,
- CTA visibility,
- legibility,
- motion not obstructing comprehension,
- content completeness.

### 6. Technical Feel and Stability — 5
Judge:
- obvious frame drops,
- visual glitches,
- load behavior,
- input responsiveness,
- broken layout/interaction.

## Pass Rule

Desktop homepage passes only when:
- total >=85/100,
- Motion >=25/30,
- Hero >=16/20,
- Cohesion >=16/20,
- no major content is missing,
- no obvious stutter or broken interaction remains.

A bug-free implementation can still fail.

## Deferred RWD Scope

Do not execute mobile QA in the default desktop stage. When the user later explicitly requests RWD, create a separate acceptance scope and then evaluate information clarity, touch/scroll feel, runtime stability, visual continuity and appropriate simplification. Do not infer mobile approval from the 2560×1280 result.

## Review Method

For every review:
1. score each category,
2. cite concrete evidence from the current build,
3. identify the top three defects by impact,
4. propose exact revisions,
5. re-score after revisions.

Never inflate scores to move the project forward.


## POC / Vertical Slice Gate

Before full production, confirm the slice proves at 2560×1280: brand/IP fidelity, spatial depth, cinematic motion without dizziness, useful interaction, acceptable desktop performance, conversion clarity, and a scalable implementation architecture. A POC may fail even when visually attractive if any of these remain unresolved.
