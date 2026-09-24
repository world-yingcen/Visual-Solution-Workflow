# Detailed Production Specification

## Purpose

Translate an approved design into an implementation-grade specification with low ambiguity. This is the point where detail becomes dense.

For CREATE Mode, use this after direction approval. Before the core slice, specify only that slice against a working visual/motion system. After browser validation and slice approval, expand the proven system into full production specifications. Do not wait for whole-site specification completion to test the central experience.
For RECREATE Mode, use it after the reference/source audit and fidelity analysis.

The specification must be detailed enough that a coding agent does not need to invent core visual, motion, layering, content, or interaction decisions.

## Detail Principle

Increase precision as decisions stabilize:
- Creative exploration: detailed goals and constraints, open solutions.
- Design development: detailed visual, spatial, motion, and narrative system.
- Production specification: detailed behavior, assets, layering, states, technical responsibilities, mistakes to avoid, and observable acceptance criteria.

Do not confuse precision with over-prescription. Specify what must remain true; allow implementation freedom where multiple technical solutions can preserve the approved experience.

# Required Production Spec Structure

## 1. Experience Intent

State:
- what the page/site is trying to make the user feel,
- the core interaction model,
- the visual/spatial premise,
- the role of scroll, pointer, touch, media, and WebGL,
- the commercial/information objective.

Keep this concise and project-specific.

## 2. Preserve Brand / Source Quirks

List unusual details that must survive implementation because they contribute to identity or fidelity.

Examples of categories:
- unconventional typography or variable-font settings,
- asymmetric spacing,
- nonstandard section heights,
- unusual sticky behavior,
- custom cursor behavior,
- odd but intentional layer order,
- specific naming/label patterns,
- unconventional masks, rails, counters, progress UI,
- deliberate timing or motion quirks,
- brand-specific micro-interactions.

In CREATE Mode, call these `Preserve Brand / Design Quirks`.
In RECREATE Mode, call these `Preserve Source Quirks`.

Do not invent quirks just to fill the section.

## 3. Critical Design / Fidelity Constraints

Write non-negotiables as explicit constraints.

Possible categories:
- canonical brand/IP restrictions,
- required content and copy,
- exact or approved fonts,
- palette constraints,
- no-placeholder requirements,
- live 3D vs media fallback requirements,
- layer ownership,
- scroll model,
- interaction availability,
- 2560×1280 viewport behavior,
- forbidden additions or reinterpretations.

In RECREATE Mode, prefer exact fidelity language when evidence exists.
In CREATE Mode, protect approved design intent without pretending every value is immutable.

## 4. Tech Stack / Dependency Intent

Specify only dependencies that are actually justified by the approved design or source.

Include, when relevant:
- framework/runtime,
- animation engine,
- smooth-scroll system,
- WebGL/3D engine,
- post-processing,
- font source,
- media handling,
- loader/compression requirements,
- required versions only when version fidelity materially matters.

Do not add Three.js, GSAP, Lenis, shaders, or postprocessing by default.

## 5. Global Visual System

Define implementation-relevant global variables:
- color tokens and their functions,
- typography families / axes / weight / tracking behavior,
- spacing/gutter logic,
- radii/borders,
- lighting/atmosphere,
- material language,
- noise/grain rules,
- persistent UI treatment,
- reduced-motion implications.

Use exact values when approved or source-derived. Otherwise use bounded design intent.

## 6. Asset Map

Create an explicit map of all production assets.

For each asset record:
- asset ID / role,
- source path or URL,
- format,
- aspect ratio / dimensions if relevant,
- scene ownership,
- preprocessing needs,
- canonical/IP restrictions,
- fallback.

Include as needed:
- images,
- video,
- GLB/GLTF,
- textures,
- HDRI,
- SVG paths,
- logos,
- icons,
- audio,
- depth maps,
- masks,
- generated support assets.

Do not silently replace missing approved assets.

## 7. Vector / Shape Data

When exact vector geometry matters, record:
- viewBox,
- path data,
- stroke/fill rules,
- masks/clipping paths,
- animation ownership.

Omit this section when no exact vector geometry is required.

## 8. Layer Stack / Positioning Map

Always define the major compositing order for immersive pages.

For each layer state:
- semantic role,
- DOM/Canvas ownership,
- positioning mode (`fixed`, `sticky`, `absolute`, `relative`),
- z-index or relative stacking order,
- pointer-events behavior,
- blend/mask relationship,
- whether it persists across scenes.

Example form:
- z-0 Atmosphere / fixed
- z-1 WebGL canvas / fixed
- z-2 spatial typography / fixed or section-scoped
- z-3 story DOM / relative
- z-5 navigation / fixed
- z-10 cursor / fixed

Do not reuse this exact stack mechanically. Derive the map per project.

## 9. Global Scroll / State Architecture

Define how global progress becomes scene state.

State:
- native scroll / smooth scroll / virtual scroll policy,
- master experience controller behavior,
- scene progress ownership,
- scroll-to-camera mapping,
- persistent state across sections,
- reverse-scroll behavior,
- interruption behavior,
- route/page transition behavior if relevant.

Avoid unrelated one-off ScrollTriggers when a shared experience controller is more coherent.

## 10. Section / Scene by Section Specification

For each scene in the current implementation scope, define the following. Keep unproven future scenes at outline level until the core slice is validated.

### A. Scene Identity
- Scene name / ID
- Purpose
- User takeaway
- Required copy / CTA
- Source content
- Canonical assets

### B. Layout / Composition
- desktop composition,
- focal hierarchy,
- viewport coverage,
- section/sticky height when important,
- alignment/grid logic,
- negative space,
- overlap/depth relationships.

### C. Initial State
Describe what exists before the user begins interacting or scrolling through the scene.

### D. Scroll / Timeline States
When scroll drives the scene, use normalized progress or meaningful trigger ranges.

For each range specify:
- camera position/target/FOV/zoom intent,
- object position/rotation/scale,
- DOM transforms,
- mask/clip behavior,
- opacity/visibility,
- lighting changes,
- material/shader state,
- text readability,
- transition handoff.

Do not force normalized values if source-trigger positions or natural document flow are more appropriate.

### E. Desktop Pointer / Keyboard Interaction
Specify:
- trigger,
- target,
- response,
- magnetic/drag/hover/click behavior,
- priority relative to scroll,
- pointer-events rules,
- keyboard alternative where the control is interactive,
- disabled states.

### F. Motion Choreography
Define:
- entry sequence,
- focal sequence,
- hold/read interval,
- exit sequence,
- overlap with adjacent scenes,
- speed relationships between depth layers,
- motion character/easing family,
- camera-led vs object-led vs typography-led behavior.

### G. DOM / Canvas / SVG / Media Ownership
For every major element, state who renders it and why.

### H. Technical Behavior
Specify only behavior needed for fidelity:
- scene lifecycle,
- preloading,
- media play/pause,
- shader/material state,
- physics/spring values when approved or source-derived,
- data/state synchronization,
- fixed-target viewport sizing behavior,
- cleanup/disposal.

### I. 2560×1280 Viewport State
Define the exact desktop composition and behavior at 2560×1280:
- viewport coverage and safe areas,
- focal object crop,
- text line breaks and reading zone,
- sticky/pinned distance,
- pointer behavior,
- performance fallback that still preserves the desktop concept.

Do not add responsive adaptation in this stage. If the user later requests RWD, add it as a separate specification revision.

### J. Acceptance Criteria
Write observable pass/fail conditions for the scene.

## 11. Global Motion / Interaction Rules

Document cross-site rules such as:
- split text method,
- scroll synchronization,
- cursor model,
- spring/physics behavior,
- hover grammar,
- mask/reveal behavior,
- camera parallax,
- media autoplay rules,
- theme transitions,
- number/counter behavior,
- loading/boot sequence.

Do not duplicate per-scene details unnecessarily.

## 12. Desktop Viewport Strategy

Define the 2560×1280 composition, input model and performance expectations at the system level. Record browser, CSS viewport, zoom and device-pixel ratio when they affect evidence. Tablet／Mobile are excluded until the user explicitly opens a separate RWD scope.

## 13. Performance Budget / Risk Map

Identify meaningful risks:
- texture memory,
- GLB complexity,
- shader/postprocessing cost,
- video decode,
- excessive observers/triggers,
- layout thrashing,
- high DPR,
- CPU physics,
- preload waterfalls,
- oversized fonts/assets.

For each risk include:
- severity,
- likely symptom,
- mitigation,
- fallback.

## 14. Common Mistakes to Avoid

Every Production Specification must include a project-specific `Common Mistakes to Avoid` section.

These are failure patterns the coding agent is likely to introduce while trying to simplify, generalize, or "improve" the design.

Examples:
- do not replace the variable font with static weights,
- do not move the WebGL layer above primary copy,
- do not add gradients/shadows absent from the approved design,
- do not turn every section into the same fade-up animation,
- do not restyle canonical characters or products,
- do not make pointer-blocking overlays cover the 3D interaction,
- do not replace a continuous scene transition with hard section cuts,
- do not begin RWD or mobile work in the default desktop-only stage.

Generate these from the actual project. Never paste a generic list without relevance.

## 15. Implementation Requirements

Collect implementation-level non-negotiables in one place.

Examples:
- exact asset URLs,
- required initialization/boot sequence,
- mandatory component/state behavior,
- canvas sizing behavior,
- visibility/observer rules,
- reduced-motion handling,
- accessibility behavior,
- browser targets,
- explicit no-placeholder/no-substitution rules,
- repository constraints.

This section should make hidden assumptions explicit before Codex starts coding.

## 16. Acceptance Criteria

Create a final global acceptance checklist with observable criteria.

Cover:
- visual fidelity / brand fidelity,
- content completeness,
- typography,
- layer ordering,
- scroll and transition feel,
- interaction availability,
- runtime stability,
- target viewport behavior,
- reduced motion,
- console/runtime errors,
- performance risks,
- no unapproved additions.

Avoid vague checks such as "looks premium" unless paired with concrete evidence.

# Sequence-Level Continuity

For connected scenes also define:
- shared camera logic,
- continuity objects,
- persistent UI,
- global color/lighting shifts,
- preload order,
- cross-scene timing,
- transition ownership,
- reverse-scroll behavior,
- state restoration.

The final spec must read like one designed system, not a stack of unrelated animated sections.
