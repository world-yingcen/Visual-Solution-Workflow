# Motion and Technical Architecture

## Technology Principle

Select technology after the experience is defined.

Typical candidates:
- Next.js / React for application, content, routing, SEO, UI,
- GSAP / ScrollTrigger for choreography and timelines,
- Lenis or equivalent only when smooth-scroll behavior materially improves feel,
- Three.js / React Three Fiber / Drei for spatial scenes and WebGL,
- postprocessing for selective visual treatment,
- GLSL shaders for effects that need GPU image/geometry processing,
- video/image sequences when prerendered cinematic media is more efficient,
- WebGPU only when justified.

## DOM / Canvas / Hybrid

Default principle: Canvas creates the world; DOM communicates information.

Use DOM for navigation, headings, body copy, price, product facts, plans, CTA, forms, address, FAQ, SEO content, and accessibility-critical UI.

Use Canvas/WebGL for camera, spatial scenes, particles, fog, distortion, depth, lighting, environments, and shader-driven transitions.

Use hybrid/2.5D for characters, artwork, product displays, layered photography, depth maps, image shaders, and scene reveals.

## Motion Primitives

Prefer reusable primitives over one-off animation code. Examples:
- CameraTravel
- DepthParallax
- TextReveal
- CharacterReveal
- SceneTransition
- ImageDistortion
- EnergyHover
- Atmosphere
- ParticleReaction
- RealityTransition
- LoadingTransition
- PageTransition

Only include primitives needed by the selected direction.

## Master Scroll Architecture

Avoid many unrelated ScrollTriggers controlling isolated sections.

Prefer a shared experience model:

Scroll Progress
-> Experience Controller
-> Current Scene / Scene Progress / Transition Progress
-> Camera / WebGL / Typography / Particles / Shader / DOM

Treat scroll as the experience timeline when the project uses continuous cinematic scrolling.

## Progressive Enhancement

For the default stage, tune the selected architecture and performance at 2560×1280. Do not add device tiers or Mobile variants unless the user explicitly opens a later RWD scope.

Support where applicable:
- prefers-reduced-motion,
- WebGL-unavailable fallback,
- semantic DOM,
- keyboard accessibility,
- SEO content,
- lazy loading,
- texture/model compression,
- resource disposal.

Existing responsive code may remain, but desktop implementation work must not silently claim or redefine its behavior.
