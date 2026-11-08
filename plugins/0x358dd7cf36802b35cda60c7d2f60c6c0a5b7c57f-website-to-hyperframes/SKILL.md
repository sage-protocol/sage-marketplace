---
name: website-to-hyperframes
description: "Capture a website and create a HyperFrames video from it. Use when: (1) a user provides a URL and wants a video, (2) someone says 'capture this site', 'turn this into a video', 'make a promo from my site', (3) the user wants a social ad, product tour, or any video based on an existing website, (4) the user shares a link and asks for any kind of video content. Even if the user just pastes a URL — this is the skill to use."
---

# Website to HyperFrames

Capture a website, then produce a professional video from it.

Users say things like:

- "Capture https://... and make me a 25-second product launch video"
- "Turn this website into a 15-second social ad for Instagram"
- "Create a 30-second product tour from https://..."

The workflow has 7 steps. Each produces an artifact that gates the next.

---

## Step 1: Capture & Understand

**Read:** [references/step-1-capture.md](references/step-1-capture.md)

Run the capture, read the extracted data, and build a working summary using the write-down-and-forget method.

**Gate:** Print your site summary (name, top colors, fonts, key assets, one-sentence vibe).

---

## Step 2: Write DESIGN.md

**Read:** [references/step-2-design.md](references/step-2-design.md)

Write a simple brand reference for the captured website. 6 sections, ~90 lines. This is a cheat sheet, not the creative plan — that comes in Step 4.

**Gate:** `DESIGN.md` exists in the project directory.

---

## Step 3: Write SCRIPT

**Read:** [references/step-3-script.md](references/step-3-script.md)

Write the narration script. The story backbone. Scene durations come from the narration, not from guessing.

**Gate:** `SCRIPT.md` exists in the project directory.

---

## Step 4: Write STORYBOARD

**Read:** [references/step-4-storyboard.md](references/step-4-storyboard.md)

Write per-beat creative direction: mood, camera, animations, transitions, assets, depth layers, SFX. This is the creative north star — the document the engineer follows to build each composition.

**Gate:** `STORYBOARD.md` exists with beat-by-beat direction and an asset audit table.

---

## Step 5: Generate VO + Map Timing

**Read:** [references/step-5-vo.md](references/step-5-vo.md)

Generate TTS audio, transcribe for word-level timestamps, and map timestamps to beats. Update STORYBOARD.md with real durations.

**Gate:** `narration.wav` (or .mp3) + `transcript.json` exist. Beat timings in STORYBOARD.md updated.

---

## Step 6: Build Compositions

**Read:** The `hyperframes` skill (load it — every rule matters)
**Read:** [references/step-6-build.md](references/step-6-build.md)

Build each composition following the storyboard. After each one: self-review for layout, asset placement, and animation quality.

**Gate:** Every composition has been self-reviewed. No overlapping elements, no misplaced assets, no static images without motion.

---

## Step 7: Validate & Deliver

**Read:** [references/step-7-validate.md](references/step-7-validate.md)

Lint, validate, snapshot, preview. Deliver the localhost Studio project URL
(`http://localhost:<port>/#project/<project-name>`) to the user first — only
render to MP4 on explicit request. Do not treat `index.html` as the project
handoff link; it is source-code context only.

**Gate:** `npx hyperframes lint` and `npx hyperframes validate` pass with zero errors, and the final response includes the active Studio project URL.

---

## Quick Reference

### Video Types

| Type                  | Duration | Beats | Narration              |
| --------------------- | -------- | ----- | ---------------------- |
| Social ad (IG/TikTok) | 10-15s   | 3-4   | Optional hook sentence |
| Product demo          | 30-60s   | 5-8   | Full narration         |
| Feature announcement  | 15-30s   | 3-5   | Full narration         |
| Brand reel            | 20-45s   | 4-6   | Optional, music focus  |
| Launch teaser         | 10-20s   | 2-4   | Minimal, high energy   |

### Format

- **Landscape**: 1920x1080 (default)
- **Portrait**: 1080x1920 (Instagram Stories, TikTok)
- **Square**: 1080x1080 (Instagram feed)

### Reference Files

| File                                                     | When to read                                                                                                                                                                   |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [step-1-capture.md](references/step-1-capture.md)        | Step 1 — reading captured data                                                                                                                                                 |
| [step-2-design.md](references/step-2-design.md)          | Step 2 — writing DESIGN.md                                                                                                                                                     |
| [step-3-script.md](references/step-3-script.md)          | Step 3 — writing the narration script                                                                                                                                          |
| [step-4-storyboard.md](references/step-4-storyboard.md)  | Step 4 — per-beat creative direction                                                                                                                                           |
| [step-5-vo.md](references/step-5-vo.md)                  | Step 5 — TTS, transcription, timing                                                                                                                                            |
| [step-6-build.md](references/step-6-build.md)            | Step 6 — building compositions with self-review                                                                                                                                |
| [step-7-validate.md](references/step-7-validate.md)      | Step 7 — lint, validate, snapshot, preview                                                                                                                                     |
| [techniques.md](../hyperframes/references/techniques.md) | Steps 4 & 6 — 11 visual techniques with code patterns (SVG drawing, Canvas 2D, 3D, typography, Lottie, video, typing, variable fonts, MotionPath, transitions, audio-reactive) |


<!-- REFERENCES -->

## Reference: step-3-script.md

# Step 3: Write the Narration Script

**Before writing, re-read DESIGN.md** — specifically the Overview and Components sections. The script should reference real product features, real stats, and real components that the website highlights. Use exact numbers from `capture/extracted/visible-text.txt`.

The script is the backbone. Everything downstream — scene durations, animation timing, beat pacing — comes from the narration. Write it before the storyboard.

Save as `SCRIPT.md` in the project directory.

Read [../../hyperframes/references/narration.md](../../hyperframes/references/narration.md) for the full narration guide.


## Reference: step-4-storyboard.md

# Step 4: Write the Storyboard

**Before writing anything, fully re-read these files:**

- **DESIGN.md** — your color palette, font rules, components, Do's/Don'ts. Every creative decision must be grounded in this brand identity. If it says "white backgrounds with purple accent" — plan light scenes, not dark moody ones.
- **`capture/extracted/asset-descriptions.md`** — read EVERY line. This is your menu of available visuals. Each line describes what the image actually shows (e.g., "translucent ribbons in orange, pink, and purple on white background" or "a high-speed train under a dark starry sky"). Use these descriptions to decide which assets belong in which beat. Assets you don't understand from the description — view them directly before assigning.
- **[techniques.md](../../hyperframes/references/techniques.md)** — 11 visual techniques (SVG path drawing, Canvas 2D art, CSS 3D, per-word typography, Lottie, video compositing, typing effect, variable fonts, MotionPath, velocity transitions, audio-reactive). Pick 2-3 per beat and specify them in the storyboard.

The storyboard is the creative north star. It tells the engineer exactly what to build for each beat — mood, camera, animations, transitions, assets, sound. Write it as if you're briefing a motion designer who's never seen the website.

Save as `STORYBOARD.md` in the project directory.

---

## Global Direction

Every STORYBOARD.md starts with global settings:

```markdown
**Format:** 1920×1080
**Audio:** [TTS provider] voiceover + underscore + SFX
**VO direction:** [voice character — e.g., "mid-age male, calm confident delivery,
Apple keynote register — economy of words, silence between sentences is a feature"]
**Style basis:** DESIGN.md (brand colors, fonts, components from the captured site)
```

**Global guardrails** — read [video-composition.md](../../hyperframes/references/video-composition.md) first. It defines the medium rules: density, color presence, scale, frame composition, and how design.md is brand truth not layout spec. Then apply these capture-specific additions:

- Use as many captured assets as the creative vision allows. Scatter framework icons around a dashboard. Layer enterprise photos behind stats. Use product screenshots as floating cards. The assets exist — use them generously.
- Use at least 2-3 different techniques from techniques.md per beat — not across the whole video, per beat. Don't default to basic fade/scale/opacity — mix in SVG path drawing, CSS 3D transforms, typing effects, counter animations, canvas procedural art. Each beat should feel like its own visual world.

**Underscore/music direction** (if applicable):

- Describe the mood, reference artists, when it swells or drops
- Example: "Minimal electronic. Warm sustained pad already playing when the video starts. Sits underneath everything, never competing with VO. Swells gently during the flex section, drops to near-nothing for the comparison, resolves on a final chord."

---

## Asset Audit

Before writing any beats, audit every captured asset. Print this table:

| Asset                          | Type       | Assign to Beat | Role                                  |
| ------------------------------ | ---------- | -------------- | ------------------------------------- |
| wave-fallback-desktop.png      | Hero image | Beat 1         | Full-bleed animated background        |
| enterprise-accordion-hertz.png | Photo      | Beat 3         | Enterprise credibility, Ken Burns pan |
| stripe-logo.svg                | SVG        | Beat 1, Beat 5 | Brand mark opener + closer            |
| datavizstatic3x.png            | Data viz   | Beat 3         | Supporting visual behind stats        |
| icon-3.svg                     | Icon       | SKIP           | Decorative, too small                 |

**Minimum utilization:**

- At least 50% of product screenshots and hero images must appear
- Brand logo appears in the first AND last beat
- The site's signature visual (gradient wave, hero illustration, key product UI) must appear — it's the most recognizable brand element
- Maximum 2 consecutive text-only beats. The 3rd must contain a visual asset
- Opening beat must contain a visual asset, not text-only

---

## Per-Beat Direction

Read [beat-direction.md](../../hyperframes/references/beat-direction.md) for the general beat template: concept, mood, animation choreography (energy verbs), transitions (shader vs CSS vs hard cut decision matrix), depth layers, SFX cues, rhythm planning, and velocity-matched transitions.

In the capture pipeline, each beat also includes:

### VO cue

Which narration line plays over this beat.

### Visual description

What the viewer sees — described cinematically, not as CSS specs. Use camera language (pan, zoom, drift, settle). Describe at least 5 visual elements, not just text + background. Think in layers — what's moving in the foreground, midground, background simultaneously?

### Assets

Which captured files to use, referenced by filename:

- "Background: `capture/assets/wave-fallback-desktop.png` — full-bleed, slow zoom 1→1.04 over beat duration"
- "Logo: `capture/assets/svgs/stripe-logo.svg` — centered, fades in at 0.5s"
- "Enterprise photo: `capture/assets/enterprise-accordion-hertz.png` — Ken Burns pan, 70% opacity overlay"

---

## Production Architecture

Include this file tree at the bottom of the storyboard:

```
project/
├── index.html                    root — VO + underscore + beat orchestration
├── DESIGN.md                     brand reference (from Step 2)
├── SCRIPT.md                     narration text (from Step 3)
├── STORYBOARD.md                 THIS FILE — creative north star
├── transcript.json               word-level timestamps (from Step 5)
├── narration.wav                 TTS audio (from Step 5)
├── capture/                      captured website data (from Step 1)
│   ├── screenshots/
│   ├── assets/
│   │   ├── svgs/
│   │   ├── fonts/
│   │   ├── lottie/
│   │   └── videos/
│   ├── extracted/
│   │   ├── tokens.json
│   │   ├── visible-text.txt
│   │   ├── asset-descriptions.md
│   │   ├── animations.json
│   │   ├── assets-catalog.json
│   │   └── detected-libraries.json
│   ├── AGENTS.md
│   └── CLAUDE.md
└── compositions/
    ├── beat-1-hook.html
    ├── beat-2-features.html
    ├── ...
    └── captions.html
```

---

## Example: Beat-by-Beat Format

Here are three beats from a production storyboard showing the level of detail expected.

### BEAT 1 — COLD OPEN (0:00–0:05)

**VO:** "Your AI agent already knows how to make videos."

**Concept:** We're already in motion when the video starts. No title card, no fade from black. We're mid-flight over an infinite creative workspace — dozens of living compositions scattered below us like a city seen from a drone. Each one is alive, running a different animation. The message is clear before any words: this tool makes videos. Lots of them.

**Visual:** Slow smooth diagonal drift over a vast canvas (3600×2200px plane). Scattered across it: 25 composition cards at organic angles (±5-15° rotation), soft shadows, thin borders. Each card contains a DIFFERENT running animation — kinetic type, gradient morph, data viz, particle system, logo assembly, SVG drawing, shader noise, 3D rotating object. Depth-of-field: close cards slightly blurred, focal sweet-spot in mid-distance, far cards smaller and desaturated.

**Camera:** Diagonal drift top-left to bottom-right, slight 2-3° rotation over 5s. power1.inOut ease. Zoom accelerates in final second as we approach one specific card.

**Assets:** Product screenshots and logo on cards. Each card is a mini-composition with its own animation.

**SFX:** Ambient warmth pad already playing. Faint textured hum — overhearing creative activity from a distance.

---

### BEAT 5 — THE THESIS (0:20–0:24)

**VO:** "Anything a browser can render can be a frame in your video."

**Mood:** Big statement. This sentence gets its own canvas. Clean, spacious, typographic.

**Visual:** Words appear as staggered kinetic typography. "Anything a browser can render" — distinctive serif, gentle fade + rise (y: 24px → 0, opacity 0 → 1, 0.4s, power2.out). Held beat — one second of stillness. "can be a frame in your video." appears below. As the final word lands, the entire text pulses once — a brief warm flash, subtle scale bump to 101%.

**Transition OUT:** Whip pan left — x:-400, blur:24px, opacity:0.4, 0.3s power3.in

**SFX:** Silence under the first line. On the capture pulse — a soft analog shutter click.

---

### BEAT 7 — THE CONTRAST (0:38–0:44)

**VO:** "No new framework for the agent to learn. Just HTML."

**Mood:** Clean comparison. Light base. Two worlds side by side.

**Visual:** Left half: dense code, small, compressed, overwhelming. Scrolls slowly upward. Slightly desaturated. Right half: spacious HTML, syntax-highlighted, generous line spacing, inviting. On "Just HTML." — the left side folds inward along its center line, like a book closing. The right side expands to fill the frame. Warm glow rises behind it.

**Transition IN:** Zoom through — scale 0.75→1, blur 20px→0, 0.5s expo.out
**Transition OUT:** Velocity-matched upward — y:-150, blur:30px, 0.33s power2.in

**Assets:** Real framework code on the left (actual content, not lorem ipsum). Real HyperFrames HTML on the right.

**SFX:** Left side carries a faint low drone. On fold: drone cuts. Silence. Then a single clean chime as the right side expands.


## Reference: step-7-validate.md

# Step 7: Validate & Deliver

## Lint + Validate

Run in sequence. Fix all errors before proceeding to the next command.

```bash
npx hyperframes lint
npx hyperframes validate
```

`lint` checks HTML structure statically — missing attributes, timeline registration, tween conflicts, CSS transform + GSAP conflicts (including inline styles).
`validate` loads the composition in headless Chrome and catches runtime JS errors, missing assets, and failed network requests.

## Visual Verification (snapshot)

After lint and validate pass, capture snapshot frames to SEE your own output. **Always use `hyperframes snapshot`** — do not roll your own ffmpeg/headless Chrome script; the default naming (`frame-XX-at-Ys.png`) is expected by later tooling.

```bash
npx hyperframes snapshot <project-dir> --at <beat-midpoints>
```

If the snapshot command isn't available, fall back to:

```bash
npx tsx packages/cli/src/cli.ts snapshot <project-dir> --at <beat-midpoints>
```

Calculate the midpoint of each beat from your STORYBOARD.md timings. For a 4-beat video with beats at 0-5.8s, 5.8-15.0s, 15.0-22.5s, 22.5-25.3s:

```bash
npx hyperframes snapshot <project-dir> --at 2.9,10.4,18.7,23.9
```

This renders one frame per beat at the moment when content is most visible. Use timestamps where the most content is on screen — usually 60-70% into each beat, after entrances finish but before exits start. Output lands in `<project-dir>/snapshots/` with filenames like `frame-00-at-2.9s.png`.

**View every snapshot image carefully.** Don't glance and move on. For each frame, check:

**Visibility:**

- Is there visible content? All-white or all-black frames mean compositions aren't rendering.
- Can you read ALL text? White text on white/light background is invisible. Dark text on dark background is invisible. Every text element needs contrast against what's directly behind it.
- Are images and assets showing? Empty space where an image should be means a path issue or missing file.

**Positioning and layout:**

- Do background images fill the entire frame? If an image only covers half the screen, the `object-fit`, `width`, `height`, or position values are wrong.
- Are elements where the storyboard says they should be? Compare the snapshot to the beat description.
- Is there too much empty/dead space? If more than 40% of the frame is a flat solid color with nothing on it, the composition is sparse.
- Are elements overlapping incorrectly? Text over text, or content bleeding off the edges?

**Visual quality:**

- Are overlays too heavy? If a background image is barely visible through a dark overlay, reduce the overlay opacity.
- Is the visual hierarchy clear? One dominant element per frame, supporting elements secondary.
- Do the colors match DESIGN.md? Check actual rendered colors against what was planned.

**Code vs. rendered verification:**

- For each beat, check: does the snapshot show the assets you referenced in the HTML? If a composition has `<img src="...wave.png">` but the snapshot shows no wave — the image isn't loading, the path is wrong, or it's hidden behind another element.
- If a snapshot shows nothing at a timestamp, try a slightly different time (1-2 seconds later). Compositions may still be in entrance animations.
- The snapshot command is fast — run it multiple times at different timestamps if needed.

If any frame has issues, go back to Step 6 and fix that composition before proceeding.

## Preview

```bash
npx hyperframes preview
```

Open the studio in a browser. Scrub through every beat.

### Handoff URL

The Studio URL is the project handoff surface. In the final response, report the
active preview URL with the project hash:

```text
http://localhost:<port>/#project/<project-name>
```

Use the actual port selected by `hyperframes preview` and the project name shown
by the preview command. If you run `hyperframes preview --port 3017` for a
project directory named `codex-openai-video`, the project URL is:

```text
http://localhost:3017/#project/codex-openai-video
```

Do **not** present `index.html` as the project link. `index.html` is the source
file for agents and editors; the user-facing project is the running HyperFrames
Studio preview. You may include source file links as secondary context, but the
primary "Project" or "Preview" line must be the localhost Studio URL.

If a render was also requested, still include the Studio URL first so the user
can scrub and inspect the project. Include the MP4 path as the rendered output,
not as a replacement for the project URL.

## Render (on-demand only)

**Do NOT render automatically as part of the pipeline.** Preview is the delivery — the user scrubs, spots anything they want tweaked, and you iterate. Rendering to MP4 takes minutes of wall-clock time per pass and is wasted work if the user wants changes.

Only run `hyperframes render` when the user **explicitly asks** — e.g. "render it", "make the final", "export the MP4", "I'm happy, produce the file". Until then, stop at preview + snapshots.

When the user does ask to render, always pass `--output renders/<project-name>.mp4` so the final file has a predictable, human-readable name. The CLI default is timestamped (`<project>_YYYY-MM-DD_HH-MM-SS.mp4`) which is hard to reference from docs or later iterations.

```bash
npx hyperframes render --output renders/<project-name>.mp4
```

Example: `npx hyperframes render --output renders/stripe-launch.mp4`

For social-media vertical output, check `npx hyperframes render --help` for viewport/format flags.


## Reference: step-6-build.md

# Step 6: Build Compositions

**Before building, fully re-read these files:**

- **DESIGN.md** — your color palette, fonts, components, and Do's/Don'ts. Every composition must use EXACT hex colors and font families from this file. If it says "white backgrounds" — use white, not dark.
- **STORYBOARD.md** — the beat-by-beat plan you're executing. Each beat specifies assets, animations, transitions, and which techniques to use.
- **`capture/extracted/asset-descriptions.md`** — when the storyboard assigns an asset to a beat, re-read the description to understand what it shows and how to position/style it correctly.
- **[techniques.md](../../hyperframes/references/techniques.md)** — code patterns for the 10 visual techniques. When the storyboard says "SVG path drawing" or "per-word kinetic typography" — read the code pattern from this file and adapt it.
- **transcript.json** — word-level timestamps that drive scene durations.

**Split the work: spawn a sub-agent for each beat.** By this step your context is full of captured data, DESIGN.md, SCRIPT, STORYBOARD, and transcript. Building compositions on top of all that means the detailed rules below compete with thousands of tokens of prior work. Each sub-agent gets a fresh context focused on one beat — dramatically better output.

**How to dispatch each sub-agent:**

Pass file PATHS, not file contents. The #1 failure mode is reading an asset file and pasting its SVG/image data into the sub-agent prompt. The sub-agent then uses inline content instead of referencing the file on disk. Same with fonts — pass the local woff2 path, don't substitute Google Fonts.

```
Build the composition for beat 1. Save to compositions/beat-1-hook.html.

STORYBOARD for this beat:
[paste the beat section from STORYBOARD.md]

ASSETS — reference by path, do NOT read/inline the file contents:
- Logo: <img src="../capture/assets/favicon.svg"> (top-left, 40x40px)
- Hero image: <img src="../capture/assets/hero-bg.png"> (full-bleed background)
- Noise texture: ../capture/assets/noise.png (full-frame overlay, 3% opacity)

FONTS — use @font-face with the captured font files, NOT Google Fonts:
@font-face { font-family: 'BrandFont'; src: url('../capture/assets/fonts/BrandFont-Regular.woff2'); }

Read DESIGN.md for exact colors and Do's/Don'ts.
Read techniques.md for animation code patterns.
Load the `hyperframes` skill for composition structure rules.
```

After each sub-agent finishes, verify the composition references `../capture/assets/` — if it used inline SVGs or Google Fonts instead of the captured files, fix it before moving on.

Load the `hyperframes` skill first — it has the rules for data attributes, timeline contracts, deterministic rendering, and layout. Everything below supplements those rules, not replaces them.

---

## Per-Composition Process

For each beat in the storyboard:

### 1. Read the beat's storyboard section

Know the mood, visual description, assets, animation choreography, transition, and SFX before writing any HTML.

### 2. Build the static end-state first

Position every element where it should be at its **most visible moment** — the frame where everything is fully entered and correctly placed. Write this as static HTML+CSS. No GSAP yet.

This is the "Layout Before Animation" principle from the compose skill. The CSS position is the ground truth. Animations describe the journey to and from it.

### 3. Verify the static layout

Look at it. Check:

- Are elements where the storyboard says they should be?
- Are depth layers present (foreground / midground / background)?
- Do any elements overlap unintentionally?
- Are assets sized correctly? (hero images should fill 50-70% of frame, not sit at 100x100px)

### 4. Add entrance animations

Use `gsap.from()` — animate FROM offscreen/invisible TO the CSS position. The CSS position is where the element ends up.

### 5. Add mid-scene activity

Every visible element must have continuous motion. A still image on a still background is a JPEG with a progress bar.

| Element type                           | Mid-scene activity                                                                                                                           |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Image / screenshot                     | Slow zoom (scale 1→1.03), slow pan, or Ken Burns                                                                                             |
| Stat / number                          | Counter animates from 0 to target                                                                                                            |
| Logo grid                              | Subtle shimmer sweep, or gentle scale pulse                                                                                                  |
| Any persistent element                 | Subtle float (y ±4-6px, sine.inOut, yoyo)                                                                                                    |
| Logo / CTA (with music or dramatic VO) | Audio-reactive scale/glow — bass pulses the logo (3–4%), treble glows the CTA. See technique #11 in `techniques.md` for the sampling pattern |

### 6. Add exit / transition

Check the storyboard's transition specification for this beat:

- **CSS transition**: implement the exit animation (e.g., `y:-150, blur:30px, 0.33s power2.in`). The next composition handles its own entry.
- **Shader transition**: no exit animation needed — the shader handles the blend. Read `packages/shader-transitions/README.md` for the API, available shaders, and setup. The package handles WebGL init, capture, and GSAP integration — do not copy raw GLSL manually.
- **Hard cut**: no exit animation. The scene simply ends.

For all CSS transition types and their GSAP implementations, read `skills/hyperframes/references/transitions/catalog.md`.

### 7. Asset cross-reference

Before self-review, verify you actually used the assets you planned to:

1. Open STORYBOARD.md and find this beat's asset assignments
2. List every asset that was assigned to this beat
3. Search the composition HTML for each filename (e.g., grep for "wave-fallback-desktop")
4. If any assigned asset is missing from the HTML, add it now
5. Check for the inline anti-pattern: if the HTML contains `<svg xmlns=` or `data:image/` but no `../capture/assets/` references, the assets were inlined instead of referenced. Replace inline content with `<img src="../capture/assets/filename.svg">`
6. Check fonts: if the HTML uses `fonts.googleapis.com` but there are captured fonts in `capture/assets/fonts/`, replace with `@font-face` pointing to the local files (e.g., `src: url('../capture/assets/fonts/BrandFont-Regular.woff2')`)

This step catches the two most common failures: compositions ending up text-only, and assets being inlined instead of file-referenced.

### 8. Self-review

After building the composition, check WITH ACTUAL CODE:

- [ ] Asset cross-reference passed (step 7 above — every assigned asset is in the HTML)
- [ ] Elements are where the storyboard says they should be (no misplacement)
- [ ] No overlapping text (text covering text is always ugly)
- [ ] Depth layers present (2+ layers minimum)
- [ ] Every visible element has mid-scene activity (not just entrance + exit)
- [ ] Font sizes above minimum (20px body text, 16px labels — sub-14px is unreadable after encoding)
- [ ] No full-screen dark linear gradients (H.264 creates visible banding — use solid + localized radial glows)
- [ ] Timeline registered: `window.__timelines["comp-id"] = tl`
- [ ] Colors match DESIGN.md exactly (paste the HEX value, don't approximate)
- [ ] **Every `<template>` root element** — not just `index.html`, but every sub-composition's root — has `data-start="0"`. The linter warns `root_composition_missing_data_start` when missing. Authoring `data-duration="<beat_seconds>"` on the root is also recommended for compositions whose GSAP timeline uses repeating animations (`repeat: -1` or large `repeat: N`); without it the runtime may infer `Infinity` and stall playback. The linter flags those repeating shapes directly via `gsap_infinite_repeat` and `gsap_repeat_ceil_overshoot`.
- [ ] **Caption exits have a hard kill.** If you animate captions out with `tl.to(groupEl, { opacity: 0 }, group.end)`, follow it with `tl.set(groupEl, { opacity: 0, visibility: "hidden" }, group.end)` as a deterministic kill — per-word karaoke tweens can override the exit tween and leave captions stuck on screen. Linter: `caption_exit_missing_hard_kill`.
- [ ] **No duplicate media nodes.** If the same image/video source is referenced twice with identical `data-start` + `data-duration`, the compiler discovers it twice and can double-render. Dedupe by using a single `<img>` with appropriate z-layering, or stagger the `data-start` values. Linter: `duplicate_media_discovery_risk`.

**If `skills/hyperframes-animation-map/` is installed**, run it:

```bash
node skills/hyperframes-animation-map/scripts/animation-map.mjs <composition-dir>
```

Read the summaries. Fix every flag: offscreen, collision, invisible, pacing issues.

### 9. Move to the next composition

---

## Asset Presentation

Never embed a raw flat image. Every image must have motion treatment:

- **Perspective tilt**: use `gsap.set(el, { transformPerspective: 1200, rotationY: -8 })` + `box-shadow` — creates depth. Do NOT use CSS `transform: perspective(...)` as GSAP will overwrite it.
- **Slow zoom (Ken Burns)**: GSAP `scale: 1` → `1.04` over beat duration — makes photos cinematic
- **Device frame**: Wrap in a laptop/phone shape using CSS `border-radius` and `box-shadow`
- **Floating UI**: Extract a key element and animate it at a different z-depth for parallax
- **Scroll reveal**: Clip the image to a viewport window and animate `y` position

---

## Audio Wiring

In the root `index.html`:

- **Narration**: `<audio id="narration" src="narration.wav" data-start="0" data-duration="..." data-track-index="0" data-volume="1">`
- **Underscore/music** (if storyboard specifies): `<audio id="underscore" src="underscore.mp3" data-start="0" data-duration="..." data-track-index="3" data-volume="0.15">`
- **SFX** (if storyboard specifies): individual `<audio>` elements at specific `data-start` timestamps
- **Captions** (optional — only if user requests): sub-composition on a parallel track. Skip unless explicitly asked for.

---

## Critical Rules

These exist because the capture engine is deterministic. Violations produce broken output.

- **No `repeat: -1`** — calculate exact repeats from beat duration
- **No `Math.random()`** — use a seeded PRNG (mulberry32)
- **Register every timeline**: `window.__timelines["comp-id"] = tl`
- **Synchronous timeline construction** — no async/await wrapping timeline code
- **Never use ANY CSS `transform` for centering** — not `translate(-50%, -50%)`, not `translateX(-50%)`, not `translateY(-50%)`. GSAP animates the `transform` property, which overwrites ALL CSS transforms including centering. The element flies offscreen. Use flexbox centering instead: `display:flex; align-items:center; justify-content:center` on a wrapper div. The linter catches this (`gsap_css_transform_conflict`) but only if you run it.
- **Minimum font sizes**: 20px body, 16px labels
- **No full-screen dark linear gradients** — H.264 banding

---

## Load-bearing rules for animation authoring

Rules below came out of two independent website-to-hyperframes builds (2026-04-20) where compositions lint-clean and still ship broken — elements that never appear, ambient motion that doesn't scrub, entrance tweens that silently kill their target. The linter cannot catch these; the rules must be followed by the author.

- **No iframes for captured content.** Iframes do not seek deterministically with the timeline — the capture engine cannot scrub inside them, so they appear frozen (or blank) in the rendered output. If the source you're stylizing is a live web app, use the screenshots from `capture/` as stacked panels or layered images, not live embeds.

- **Never stack two transform tweens on the same element.** A common failure: a `y` entrance plus a `scale` Ken Burns on the same `<img>`. The second tween's `immediateRender: true` writes the element's initial state at construction time, overwriting whatever the first tween set — leaving the element invisible or offscreen with no lint warning. A secondary mechanism: `tl.from()` resets to its declared "from" state when the playhead is seeked past the timeline's end, so an element that looked correct in linear playback vanishes in the capture engine's non-linear seek. Fix one of two ways:

  ```html
  <!-- BAD: two transforms on one element -->
  <img class="hero" src="..." />
  <script>
    tl.from(".hero", { y: 50, opacity: 0, duration: 0.6 }, 0);
    tl.to(".hero", { scale: 1.04, duration: beat }, 0); // kills the entrance
  </script>

  <!-- GOOD option A: combine into one tween -->
  <script>
    tl.fromTo(
      ".hero",
      { y: 50, opacity: 0, scale: 1.0 },
      { y: 0, opacity: 1, scale: 1.04, duration: beat, ease: "none" },
      0,
    );
  </script>

  <!-- GOOD option B: split across parent + child -->
  <div class="hero-wrap"><img class="hero" src="..." /></div>
  <script>
    tl.from(".hero-wrap", { y: 50, opacity: 0, duration: 0.6 }, 0); // entrance on parent
    tl.to(".hero", { scale: 1.04, duration: beat }, 0); // Ken Burns on child
  </script>
  ```

- **Prefer `tl.fromTo()` over `tl.from()` inside `.clip` scenes.** `gsap.from()` sets `immediateRender: true` by default, which writes the "from" state at timeline construction — before the `.clip` scene's `data-start` is active. Elements can flash visible, start from the wrong position, or skip their entrance entirely when the scene is seeked non-linearly (which the capture engine does). Explicit `fromTo` makes the state at every timeline position deterministic:

  ```js
  // BRITTLE: immediateRender interacts badly with scene boundaries
  tl.from(el, { opacity: 0, y: 50, duration: 0.6 }, t);

  // DETERMINISTIC: state is defined at both ends, no immediateRender surprise
  tl.fromTo(el, { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.6 }, t);
  ```

- **Ambient pulses must attach to the seekable `tl`, never bare `gsap.to()`.** Auras, shimmers, gentle float loops, logo breathing — all of these must be added to the scene's timeline, not fired standalone. Standalone tweens run on wallclock time and do not scrub with the capture engine, so the effect is absent in the rendered video even though it looks correct in the studio preview:

  ```js
  // BAD: lives outside the timeline, never renders in capture
  gsap.to(".aura", { scale: 1.08, yoyo: true, repeat: 5, duration: 1.2 });

  // GOOD: seekable, deterministic, renders
  tl.to(".aura", { scale: 1.08, yoyo: true, repeat: 5, duration: 1.2 }, 0);
  ```

- **Hard-kill every scene boundary, not just captions.** The caption hard-kill rule above generalizes: any element whose visibility changes at a beat boundary needs a deterministic `tl.set()` kill after its fade, because later tweens on the same element (or `immediateRender` from a sibling tween) can resurrect it. Apply to every element with an exit animation:

  ```js
  tl.to(el, { opacity: 0, duration: 0.3 }, beatEnd);
  tl.set(el, { opacity: 0, visibility: "hidden" }, beatEnd + 0.3); // deterministic kill
  ```


## Reference: step-1-capture.md

# Step 1: Capture & Understand

## Run the capture

Create a project directory for your video, then capture the website into a `capture/` subfolder within it:

```bash
npx hyperframes capture <URL> -o <project-dir>/capture
```

Example: `npx hyperframes capture https://stripe.com -o videos/stripe-launch/capture`

Keeping the capture artifacts (`screenshots/`, `assets/`, `extracted/`, `AGENTS.md`, `CLAUDE.md`) in a dedicated `capture/` subfolder keeps them isolated from the later build files (`SCRIPT.md`, `STORYBOARD.md`, `DESIGN.md`, `compositions/`, `index.html`, `narration.wav`, `transcript.json`, `renders/`, `snapshots/`), which all live at `<project-dir>/` root.

For exploratory captures that aren't becoming a video yet, `-o captures/<name>` at the repo root is fine — the isolation convention only matters when you're building a video on top of the capture.

No API keys required. The capture extracts design tokens, screenshots, fonts, and assets with DOM-context descriptions automatically.

**Optional:** Set `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) in a `.env` file at the repo root for richer AI-powered image descriptions via Gemini 3.1 Flash Lite vision (~$0.001/image).

Wait for it to complete. Print how many screenshots, assets, sections, and fonts were extracted.

## Read and summarize

Read each file below. After reading each one, **write a 1-2 sentence summary** of what you learned. These summaries are your working memory — the raw file content may be cleared from context later.

### Must read (do not skip)

1. **View the scroll screenshots** — viewport-sized captures covering the full page height (the number depends on the page length). Start with:
   - `capture/screenshots/scroll-000.png` — the hero section at full 1920x1080 resolution. This is the most important image. Describe: is the background light or dark? What's the dominant visual element? What colors jump out?
   - Then scan through the rest to see the full page. Each screenshot overlaps the previous by ~30%.

   After viewing them, write 3-4 sentences describing the site's visual mood, layout patterns, color strategy, and overall feel.

2. **`capture/extracted/tokens.json`** — Note the top 5-7 colors (HEX), all font families with their weights (e.g. `Inter (400,700)` or `Sohne (100-900 variable)`), number of sections, and number of headings/CTAs.

3. **`capture/extracted/visible-text.txt`** — Each line is prefixed with the HTML tag: `[h1] Heading`, `[p] Body text`, `[a] Link text`. Use these tags to understand hierarchy — headings are key messages, paragraphs are supporting copy. Strip the `[tag]` prefix when quoting text in the script.

4. **`capture/extracted/asset-descriptions.md`** — One-line-per-file summary of all downloaded assets. Note which assets are most visually striking or useful for video (hero images, logos, product screenshots).

### Read if they exist

5. **`capture/extracted/animations.json`** — Note if the site uses scroll-triggered animations, marquees, canvas/WebGL, or named CSS animations.

6. **`capture/extracted/lottie-manifest.json`** — View each preview image at `capture/assets/lottie/previews/` to see what the animations look like.

7. **`capture/extracted/video-manifest.json`** — View each preview at `capture/assets/videos/previews/` to see what each video shows.

8. **`capture/extracted/shaders.json`** — If present, this contains the actual GLSL shader code that powers the site's WebGL visual effects (gradient waves, particle systems, noise fields). Read the fragment shaders to extract: color values used in gradients, noise algorithms, blend functions. You can recreate similar effects in your compositions using Canvas 2D or by embedding the shader patterns with a `<canvas>` + WebGL context. See the Canvas 2D and procedural art patterns in `techniques.md`.

### On-demand (read when building scenes)

9. **Individual images in `capture/assets/`** — Use `capture/extracted/asset-descriptions.md` as your index. View specific images when you need them for a beat.

10. **`capture/extracted/assets-catalog.json`** — Use to find remote URLs when you need an asset that wasn't downloaded.

### For rich captures (30+ images)

Launch a sub-agent to view all images and SVGs:

> "Read every image in capture/assets/ and every SVG in capture/assets/svgs/. For each, write one line: filename — what it shows, dominant colors, approximate size. Return the complete catalog."

Use the sub-agent's catalog as your asset reference for the rest of the workflow.

## Gate

Print your site summary before proceeding to Step 2:

- **Site:** [name]
- **Colors:** [top 3-5 HEX values with roles]
- **Fonts:** [font families]
- **Sections:** [count] sections, [count] headings, [count] CTAs
- **Key assets:** [3-5 most useful assets for video]
- **Vibe:** [one sentence describing the visual identity]


## Reference: step-5-vo.md

# Step 5: Generate VO + Map Timing

## Audition voices

Never use the first voice you find. Audition 2-3 voices with the first sentence of SCRIPT.md:

- **Kokoro** (try first — free, no API key) — `npx hyperframes tts SCRIPT.md --voice af_nova --output narration.wav`. Runs locally on CPU. Requires Python 3.10+ (macOS system Python 3.9 won't work — if it fails with an onnxruntime error, move to the next option).
- **ElevenLabs** (best voice quality, widest selection) — `mcp__elevenlabs__search_voices` to browse, `mcp__elevenlabs__text_to_speech` to generate. Does not return timestamps — transcribe separately after.
- **HeyGen TTS** (returns word timestamps automatically — saves a transcribe step) — `mcp__claude_ai_HeyGen__text_to_speech`. Use when you want timestamps without a separate transcription pass.

Pick the voice that sounds most natural and conversational. Listen for pacing — does it breathe between sentences? Does it sound like a person or a robot?

## Generate full narration

Generate the full script as `narration.wav` (or `.mp3`) in the project directory.

**Also save the exact spoken text** — with pronunciation substitutions applied (e.g., `API` → `A P I`, `$2T` → `two trillion`) — as `narration.txt` in the same directory. This is the string passed to TTS, distinct from `SCRIPT.md` which is the human-readable creative doc. Having `narration.txt` makes it trivial to regenerate the audio later with a different voice without re-deriving the substitutions. Name it exactly `narration.txt`.

## Transcribe for word-level timestamps

```bash
npx hyperframes transcribe narration.wav
```

Produces `transcript.json` with `[{ text, start, end }]` for every word. These timestamps are the source of truth for all beat durations.

## Map timestamps to beats

Go through STORYBOARD.md beat by beat. For each beat:

1. Find the first word of that beat's VO cue in `transcript.json`
2. Find the last word of that beat's VO cue
3. Set `beat.start = firstWord.start`, `beat.end = lastWord.end`
4. Add 0.3-0.5s padding at the end for visual breathing room

Update STORYBOARD.md with real durations. Replace estimated times (e.g., "0:00-0:05") with actual timestamps (e.g., "0.00-3.21s").

Beat boundaries land on word onsets — hard cuts to the VO.

## Update index.html

Update each scene slot's `data-start` and `data-duration` to match the real beat timings from the transcript. Also update the total composition duration and audio element duration.


## Reference: step-2-design.md

# Step 2: Write DESIGN.md

DESIGN.md is a **brand cheat sheet** for the captured website. It encodes the visual identity so you can reference exact colors, fonts, and patterns while writing the storyboard and compositions.

DESIGN.md is NOT the creative plan. The STORYBOARD (Step 4) drives creative direction. DESIGN.md is a reference you consult, not a document you follow slavishly.

## The 6 Sections

### `## Overview`

3-4 sentences. Describe the visual identity factually: layout patterns (bento grid, logo wall, hero section), color strategy, typography tone, overall feel. Be precise, not poetic.

### `## Colors`

5-10 key colors with HEX values from `capture/extracted/tokens.json` and their roles:

```
- **Primary Surface**: `#020204` — deep black background
- **Primary Content**: `#FFFFFF` — high-purity white for text and borders
- **Accent Warm**: `#FB923C` — orange for CTAs and highlights
```

Include semantic colors if the site uses color to differentiate product areas.

### `## Typography`

Font families with weights, roles, and any distinctive usage:

```
- **Serif**: Cormorant Garamond (Italic). Major headings, brand identity.
- **Monospace**: Geist Mono. Subheaders, labels, terminal readouts. High tracking (0.1-0.3em), all-caps.
- **Sans-Serif**: Inter. Body copy, interface elements. Small sizes (9-14px).
```

Include sizing hierarchy if notable (hero: 64px, section: 32px, body: 16px).

### `## Surface-Depth`

One paragraph on depth strategy: Does the site use borders, shadows, glassmorphism, or flat color shifts? Reference specific patterns (e.g., "1px borders at white/10 opacity" or "layered backdrop-blur with thin borders").

### `## Components`

Name every notable UI component you see in the screenshot. Be specific:

- "Cinematic Accordion" not "Cards"
- "Logo Marquee" not "Scrolling section"
- "Glass Cards with grain overlay" not "Content containers"

For each, note the distinctive visual treatment (border-radius, spacing, hover behavior).

### `## Do's and Don'ts`

3-5 rules each, derived from what the site actually does and doesn't do:

```
### Do's
- Use thin subtle borders (white/10) to separate sections
- Keep imagery desaturated with dark gradients for text readability

### Don'ts
- Do not use bright solid background colors — stay in "The Void"
- Do not use standard drop shadows — use radial glow or bloom effects
- Do not use sharp high-speed animations — all motion should be fluid
```

## Rules

- Use **exact HEX values** from `capture/extracted/tokens.json`. Do not approximate.
- Name components by what you see in the screenshot, not generic terms.
- Keep it under 100 lines. This is a cheat sheet, not a design system document.
- No "Style Prompt" section — the storyboard handles creative direction.
- No "Assets" section — `capture/extracted/asset-descriptions.md` already covers this.
- No "Motion" section — the storyboard specifies motion per-beat.

## Example

This is a real DESIGN.md from a production capture (Soulscape 2026):

```markdown
# Design System

## Overview

Soulscape 2026 is a cinematic, "high-signal" digital experience that positions itself as the vanguard of AI filmmaking. The visual personality is dark, technical, and premium, characterized by high-contrast "Flare" on "Void" (white on black) aesthetics. The layout is dense but organized, utilizing heavy horizontal layering and border-defined sections to evoke a wide-screen cinematic feel. Motion is a core tenet, with atmospheric grain overlays, shifting light leaks, and slow-moving marquees creating constant, breathing texture.

## Colors

- **Primary Surface**: `#020204` (Void) - Deep black for the entire background.
- **Primary Content**: `#FFFFFF` (Flare) - High-purity white for typography and primary borders.
- **Accent 1 (Warm)**: `#FB923C` - Orange for industry/executive tiers and primary CTAs.
- **Accent 2 (Cool)**: `#60A5FA` - Blue for creative voices and summit-focused components.
- **Subtle Overlays**: `rgba(255, 255, 255, 0.02)` to `0.08` for glass backgrounds.

## Typography

- **Serif**: Cormorant Garamond (Italic). Major headings and "Soul" brand identity. Classical cinematic contrast.
- **Monospace**: Geist Mono. Subheaders, labels, terminal readouts. High tracking (0.1-0.3em), all-caps.
- **Sans-Serif**: Inter. Body copy and interface elements. Small sizes (9-14px).

## Surface-Depth

- **Glassmorphism**: Components use backdrop-filter blur(10px) with thin borders (1px solid rgba(255, 255, 255, 0.08)).
- **Layering**: Depth via fixed global grain-overlay and localized light-leak gradients rather than box-shadows.
- **Interaction**: Hover triggers subtle translateY(-5px) and increased border opacity.

## Components

- **Cinematic Accordion**: Expanding horizontal/vertical card system where panels expand from compressed state to reveal full-bleed imagery and large serif typography.
- **HUD Explorer**: Floating mobile navigation trigger styled as a "Lens" with pulsing glow and terminal readouts.
- **Slow Marquees**: Continuous horizontal tickers for partner logos and veteran listings.
- **Glass Cards**: Content containers with subtle gradients, rounded corners (2.5rem), and high-contrast iconography.
- **Grain & Flicker**: Global CSS noise filters and holographic flicker animations on UI labels.

## Do's and Don'ts

### Do's

- Use thin subtle borders (white/10) to separate sections rather than solid color changes.
- Maintain high letter-spacing on all Geist Mono labels.
- Use serif italics for emotional or visionary statements.
- Keep imagery desaturated or stylized with dark gradients for readability.

### Don'ts

- Do not use bright solid background colors — the page must remain in "The Void."
- Do not use standard drop shadows — use radial glow or bloom effects instead.
- Do not use sharp high-speed animations — all motion should be fluid and breathing.
```

Here is a contrasting example from a light, corporate brand to show the range:

```markdown
# Design System

## Overview

Stripe's visual personality is defined by high-precision, technical sophistication, and a fluid, forward-moving motion language. The layout is dense but expertly balanced, utilizing a "canary" grid system that favors high-density data visualizations and modular bento-style layouts. The tone is authoritative and innovative, characterized by smooth CSS animations, complex SVG graphics that mimic UI dashboards, and the iconic "hero wave" background that uses layered gradients to create depth and movement.

## Colors

- **Brand Primary**: #635bff (The signature Stripe Blurple)
- **Text Solid**: #0a2540 (Deep navy for primary headings)
- **Text Soft**: #424770 (Subdued slate for descriptions and secondary text)
- **Surface Background**: #ffffff (White primary surface)
- **Surface Subdued**: #f6f9fc (Light gray for section contrast)
- **Accent Green**: #212d45 (Used in high-converting success UI graphics)
- **Accent Orange**: #ff6118 (Used for specific product highlights like Connect)
- **Accent Yellow**: #fc5 (Warm highlight used in bento cards)
- **Border Quiet**: #e6ebf1 (Soft borders for cards and dividers)

## Typography

- **Primary Font**: Sohne (sohne-var), a custom neo-grotesque that balances technical precision with approachability. Used across all headers and body copy.
- **Monospace Font**: SourceCodePro-Medium, specifically for code snippets, tabular data, and technical UI identifiers.
- **Heading Scale**: hds-heading--xxl ~3rem, hds-heading--lg ~1.5rem, hds-heading--md ~1.125rem
- **Body Scale**: Standard body text centers around 1rem (16px) with a line-height of 1.5-1.6.

## Surface-Depth

- **Shadows**: Multi-layered shadow system (e.g., 0 30px 60px -12px rgba(50,50,93,0.25)). Shadows are diffused and deep for a floating effect.
- **Borders**: Heavy use of 1px solid borders to define bento grid boundaries instead of shadows in flat sections.
- **Glass/Layering**: Navigation overlays use backdrop-filter blur(5px) with translucent white background.

## Components

- **Navigation Popover**: Animated dropdown spanning page margin with multi-column bento layouts.
- **Bento Cards**: Interactive grid-aligned containers with gradient hover effects that follow the cursor.
- **Customer Marquee**: Seamless horizontal scrolling loop of flat-colored SVG logos.
- **UI Graphics**: Custom HTML/CSS representations of the Stripe Dashboard with tabular numbers and mini-charts.
- **CTA Buttons**: Rounded-pill shapes with subtle scale transforms on hover.

## Do's and Don'ts

- **Do**: Use smooth cubic-bezier(.25, 1, .5, 1) transitions for all hover states and entering animations.
- **Do**: Maintain strict vertical alignment between iconography and text labels.
- **Don't**: Use sharp-cornered cards; always apply a border-radius.
- **Don't**: Over-saturate backgrounds; stick to white or #f6f9fc and let brand assets provide color pop.
```
