# POC / Prototype and Build Strategy

## POC Goal

Prove the hardest or most representative experience before full production.

Choose the smallest sequence that validates:
- Hero quality,
- scroll feel,
- key transition language,
- source asset depth,
- brand/IP fidelity,
- one Signature Moment,
- technical architecture,
- 2560×1280 desktop performance.

A useful POC is often Hero -> first transformation -> core scene/signature moment.

Apply [首次產出完成度基準](quality-baseline.md): include a representative real-content reading state and its transition, not just the most spectacular effect. Before expansion, compare Hero, a representative content composition and CTA as one visual system; static compositions are sufficient for this comparison. If the user requests a full homepage in the first delivery, retain that scope and plan its compositions and assets before implementation.

連續捲動的片段需包含前一場景穩定呈現、退出、下一場景完整接手，以及反向恢復。只驗證 Hero 內部漂浮或視差，不足以證明跨區塊語言成立。

Start after direction approval with slice-scoped assets and specification, not after exhaustive whole-site documents. A technical spike may use grayboxes, but the visual approval slice needs representative production assets and typography. Inspect generated/processed assets using `asset-production.md` before declaring the composition successful.

Run the slice in a browser at 2560×1280 and provide an operable preview. Inspect entry, intermediate, exit and reverse-scroll states plus actual pointer input. Do not add a small-screen feasibility case in this stage. Use `refinement-loop.md` to fix failures; only expand the proven design after slice confirmation. User-authorized changes to approval gates take precedence.

Do not spend early POC time on full navigation, FAQ, footer, all pages, or low-risk information modules unless required to test the experience.

## Validation Questions

Check:
- Can the original assets create enough depth?
- Is Three.js truly necessary?
- Can 2.5D produce a better cost/performance result?
- Is the scroll architecture smooth and understandable?
- Are shader/post effects technically viable?
- Does the experience preserve the client's visual identity?
- Does the coding architecture scale to production?

## Performance Discipline

During development:
- minimize layout thrashing,
- prefer transform/opacity for DOM animation,
- avoid unnecessary per-frame React state,
- limit heavy postprocessing,
- control texture/model resolution,
- tune DPR where appropriate,
- suspend/offload effects when offscreen,
- dispose GPU resources.

Do not approve a beautiful effect that noticeably harms scroll feel.

## Desktop-first Production Sequence

1. POC / Vertical Slice
2. Review Gate 02: QA/tuning
3. Complete desktop homepage
4. 2560×1280 Desktop QA
5. User approval
6. Hero inner page
7. Information pages
8. Desktop QA/performance polish

RWD/mobile adaptation is a separate later scope and starts only after the user explicitly requests it.
