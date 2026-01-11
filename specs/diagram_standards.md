# Variable Wing Sailplane — Diagram Standards v1.0

These rules govern *all* technical diagrams: README figures, specs, slides, posters.
If a diagram violates this, the diagram is wrong.

---

## 1. Purpose
Diagrams exist to explain **structure, motion, or constraint**.
If a line does not explain one of those, remove it.

---

## 2. Canvas & Grid
- Background: white or near-white only
- Grid: optional, construction-only
  - Spacing: 8 units
  - Opacity: 5–8%
  - Never visible in final exports

No textured backgrounds. No frames.

---

## 3. Line Weights (absolute rule)
Define base unit **x = wing bar height from logo**.

- Primary structure: **1.0x**
- Secondary structure: **0.75x**
- Reference / datum: **0.5x**
- Construction / guides: **0.25x**, dashed

Never mix arbitrary stroke weights.

---

## 4. Color Logic
Default is monochrome.

- Fixed geometry: dark gray / black
- Variable geometry: accent color
- Motion: dashed accent + arrowheads
- Limits / envelopes: light gray

If color is removed, the diagram must still read.

---

## 5. Motion Notation
Motion is **never implied**. It is drawn.

- Rotation: arc + arrowhead
- Translation: straight arrow
- Range: two bounding arcs or lines
- Hinge axis: solid line, labeled

No curved arrows without a center.

---

## 6. Views (approved set)
Only these views are allowed unless justified:

1. Top planform (primary)
2. Side elevation
3. Front section (spar / pivot)
4. Exploded axonometric (mechanism only)

No perspective renders in technical sections.

---

## 7. Labels
- Typeface: Inter Medium
- Size: small, consistent, secondary
- Orientation: horizontal only
- Alignment: left or right, never centered on lines

Use leaders sparingly. Prefer proximity.

---

## 8. What to Draw (minimum set)
Every serious iteration should have:

- Planform: min sweep / max sweep overlay
- Pivot axis location
- CG range bar
- Actuator or control linkage (abstracted)
- Sweep envelope limits

If one of these is missing, the diagram is incomplete.

---

## 9. What Not to Draw
- Shading
- Gradients
- Fake depth
- Drop shadows
- Decorative arrows
- Photographic textures

If it looks illustrative, it is not a diagram.

---

## 10. Export
- Format: SVG (master), PNG (derived)
- Stroke scaling: disabled
- Aspect ratios: consistent within a set

SVGs are source files. Do not edit PNGs.

---

## Principle
Clarity beats completeness.
If a diagram becomes crowded, split it.
