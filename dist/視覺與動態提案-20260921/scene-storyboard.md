# Scene-by-Scene Storyboard

Treat Scene as the primary experiential unit, not only Section.

Read [motion-proposal.md](motion-proposal.md) before preparing approval storyboards. Show actual start / middle / end compositions after visual approval and before the core implementation. Record motion approval separately from visual approval; existing prototype motion is not automatically accepted.

For each scene specify:
- Scene Name
- Purpose
- Source Content
- Canonical Assets
- Visual Composition
- Narrative / message
- Scroll Behavior
- Pointer / hover behavior
- Transition In
- Transition Out
- DOM Elements
- WebGL / Canvas Elements
- GSAP Responsibilities
- Shader Responsibilities
- Immersion Intensity
- Reading Zone
- Conversion / CTA role
- Performance Risk
- 2560×1280 Acceptance State
- Acceptance Criteria

## Scene Questions

Every scene must answer:
- Where is the user now?
- What should they notice first?
- What changes as scroll progresses?
- What changes from desktop pointer/keyboard interaction?
- How does the scene enter and leave?
- What information must remain readable?
- What truly requires Canvas/WebGL?
- What can remain DOM/CSS/GSAP?

The storyboard should be detailed enough for a coding agent to implement without inventing core interaction behavior.

## 相鄰場景的交接

對有連續轉場的相鄰場景，補一張具代表性的中途画面，標示前景、背景、文字及主圖的交接。記錄固定舞台與一般文件流的邊界，以及資訊列隱藏／收合後的高度、間距和下一段起點。檢查正向、反向及直接跳段是否出現空白帶、重疊或尚未可讀就離場。一般自然捲動段落只需交代間距與視覺分層，不必額外設計轉場。
