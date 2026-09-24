# Codex Implementation Handoff

## Purpose

Turn the current approved scope into an execution brief. Before the core slice, only its design and behavior need implementation detail. In Codex, execute this brief directly with available tools; do not stop at writing a prompt or ask the user to relay it. Preserve an existing authorized automatic agent pipeline when present.

Separate two categories clearly:
- **Approved design/fidelity decisions**: preserve them.
- **Implementation freedom**: choose the strongest technical solution that preserves the approved result.

## Required Handoff Structure

### 1. Objective
State exactly what must be built in this pass and what experience/fidelity must be preserved.

### 2. Mode
Declare:
- CREATE Mode,
- RECREATE Mode,
- or CREATE Mode with explicit reference constraints.

This determines how much reinterpretation is allowed.

### 3. Approved Inputs
Reference the approved:
- Creative Direction or Reference Audit,
- Experience Blueprint,
- Visual System,
- Scene Storyboard,
- Technical Architecture,
- Detailed Production Specification,
- asset map,
- repository / target route.

引用確切確認版本與畫面路徑，沿用既有提案／Blueprint 中的已確認、待確認、待試做及可微調界線。尚未驗證的數值視為試做起點，不將提案意向誤當正式動態核准。實作遇到無法保留的設計，記錄預期與實際差異、原因、替代及影響；一般參數調整依授權繼續，改變已確認方向才交使用者決策。

### 4. Non-Negotiables
Include project-specific constraints such as:
- canonical brand/IP rules,
- required content,
- preserve-source quirks,
- fidelity constraints,
- exact assets/fonts where required,
- layer stack,
- interaction availability,
- 2560×1280 desktop gate,
- no-placeholder / no-substitution rules.

### 5. Implementation Scope
State what this coding pass includes and excludes.

Prefer narrow stages:
- Vertical Slice,
- one signature sequence,
- desktop homepage,
- performance/fidelity polish.

RWD adaptation is not a default stage; include it only when the user explicitly requests it later.

Do not request the full site if the current gate only calls for a POC.

### 6. Repository Inspection Requirement
Before editing, require the coding agent to:
1. inspect the current project structure,
2. identify existing framework/dependencies,
3. identify reusable components and existing motion architecture,
4. identify conflicts with the approved specification,
5. adapt the implementation plan to the actual repository.

Do not prescribe filenames that have not been verified.

### 7. Asset / Dependency Requirements
Provide:
- exact approved asset URLs/paths,
- font sources,
- 3D/media dependencies,
- required package versions only when material,
- preprocessing requirements,
- fallback rules.

### 8. Layer Stack / Pointer Ownership
Repeat the approved layer map in compact form.

Explicitly state:
- fixed/sticky/relative ownership,
- z-order,
- pointer-events behavior,
- Canvas/DOM interaction rules.

This is mandatory for immersive/WebGL builds.

### 9. Scene Tasks
For each scene/task include:
- purpose,
- composition requirements,
- required assets,
- initial state,
- scroll/state behavior,
- interaction behavior,
- motion choreography,
- DOM/Canvas/SVG/media responsibility,
- transition behavior,
- 2560×1280 behavior,
- responsive behavior only if the user has explicitly added it to scope,
- acceptance criteria.

### 10. Global Behavior
Include only relevant cross-site rules:
- master scroll controller,
- Lenis/native scroll synchronization,
- scene lifecycle,
- motion primitives,
- cursor system,
- split text system,
- media observer behavior,
- WebGL synchronization,
- loading/boot sequence,
- reduced-motion behavior,
- cleanup/resource disposal.

### 11. Common Mistakes to Avoid
Copy the project-specific mistakes from the Production Specification and adapt them to the actual repository.

Treat this as a negative acceptance checklist.

### 12. Verification Loop
Require the coding agent to:
1. run the project,
2. verify the target page in the browser,
3. check console/runtime errors,
4. test the 2560×1280 viewport, or the user-explicit replacement desktop viewport,
5. inspect scroll continuity and input behavior,
6. verify layer/pointer ownership,
7. compare against the approved visual/motion spec,
8. fix visible regressions before reporting completion.

For RECREATE Mode, compare against the supplied reference/source rather than relying on memory.

### 13. Report Back
Require:
- what changed,
- files changed,
- what was verified,
- known deviations,
- remaining risks,
- performance concerns,
- what still needs visual review,
- recommended next stage.

## Freedom Boundary

Allow implementation changes when they preserve the approved experience.

Do not allow the coding agent to silently:
- redesign the composition,
- simplify away source quirks,
- substitute fonts/assets,
- change layer ownership,
- add decorative effects,
- alter canonical IP,
- change the primary interaction model,
- reinterpret a RECREATE brief as an original redesign.

Do not turn the handoff into line-by-line pseudocode unless a fragile algorithm actually requires it.
