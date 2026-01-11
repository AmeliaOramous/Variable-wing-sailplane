# Condor-Inspired Morphing-Wing Sailplane Drone
## Concept Specification & Design Rationale

---

## 1. Mission Overview

- **Aircraft type:** Electric sailplane-style fixed-wing drone
- **Primary mission:** Long-duration loiter and soaring (thermals)
- **Secondary mission:** Efficient dash / wind-penetration mode
- **Launch method:** Hand or assisted launch (no landing gear)
- **Recovery:** Belly landing (reinforced belly)
- **Regulatory envelope:** ≤ 400 ft AGL (U.S. consumer drone rules)

---

## 2. Design Drivers

- Efficient flight for hours at low power
- Large, high-aspect-ratio wing
- Morphing wingtip “fingers” inspired by condor primaries
- Geometry change preferred over brute-force power
- Conservative structural and speed margins

---

## 3. Mass & Power Targets

- **Target AUW:** 7 kg
- **Battery:** 12S LiPo, 12,000 mAh
  - Nominal energy: ~533 Wh
  - Usable energy (80–90%): ~425–480 Wh
- **Propulsion role:** Initial climb + dash only

### Power Budget (Electrical)
- Loiter (28 mph): ~50–85 W
- Dash (45 mph): ~95–160 W
- Climb (400 fpm): ~350–420 W
- System capability target:
  - Continuous: 800–1000 W
  - Short burst: 1200–1500 W

---

## 4. Environmental Assumptions (KXNA Reference)

- **Field elevation:** ~1,288 ft MSL
- **Design loiter altitude:** ~300 ft AGL ≈ 1,600 ft MSL

### Atmosphere Cases
**Standard day (~12°C):**
- Density ratio σ ≈ 0.95
- TAS ≈ IAS × 1.02

**Hot day (~90°F / 32°C):**
- Density altitude ≈ 4,000 ft
- Density ratio σ ≈ 0.89
- TAS ≈ IAS × 1.06

---

## 5. Speed Envelope

- **Loiter speed:** 28 mph IAS
- **Dash speed:** 45 mph IAS
- **Never exceed (Vne):** 70 mph IAS
- **Sweep activation threshold:** ≥ 35 mph IAS

---

## 6. Wing Geometry (Retracted)

- **Total fixed span:** 2.4 m
- **Per side:** 1.2 m

### Chord Distribution
| Station | Spanwise Position | Chord |
|------|------------------|-------|
| Root | 0.0 m | 0.45 m |
| Shoulder | 0.6 m | 0.35 m |
| Wrist | 1.2 m | 0.30 m |

### Fixed Wing Area
- Area per side: ~0.435 m²
- Total fixed area: ~0.87 m²

---

## 7. Morphing Wingtip “Finger”

### Geometry
- **Total finger span per side:** ~0.30 m
- **Root tuck section:** ~0.30 m (structural / fairing only)
- **Working blade:** thin, aft-biased aerodynamic surface
- **Max chord:** ≤ 0.5 × wrist chord (~0.15 m)
- **Planform:** trailing-edge dominated, feather-like but non-anatomical

### Extended Area Contribution
- Approx. added area (both sides): ~0.075 m²
- **Extended wing area total:** ~0.945 m²

### Function
- 0° sweep: span extension, induced-drag reduction, low-speed control
- 45° sweep: reduced effective span, improved high-speed behavior
- >45° sweep (future): roll-rate augmentation (experimental)

---

## 8. Sweep Mechanics

- **Type:** Planform sweep (not rotation into flow)
- **Max sweep for speed:** 45°
- **Pivot:** At wing wrist, axis normal to wing plane
- **Structure:**
  - Carbon rod main spar
  - Dual bearings (e.g., 608 class) in a pod/box
  - Worm gear drive (self-locking, low backdrive)

### Sweep Law
- ≤ 35 mph IAS: 0° sweep
- 35 → 45 mph IAS: ramp 0° → 45°
- ≥ 45 mph IAS: hold 45°

### Safety Gating
- Sweep inhibited if |n − 1| > 0.2
- Rate limit: 10–20°/s symmetric
- Differential sweep limited initially to ±10° (future)

---

## 9. Airfoil Strategy

- **Fixed wing panels:** Same airfoil across joints preferred
- **Thickness:** ~12% selected as balance between:
  - Structural depth
  - Good low-Re performance
  - Acceptable drag
- **Finger airfoil:** Fully optimized, thin, tolerant of low Reynolds number
- Thicker airfoils increase max lift but also profile drag; 12% chosen as compromise

---

## 10. Propulsion System

- **Configuration:** Tractor, folding prop
- **Prop diameter:** 20 in
- **Pitch (initial):** 10 in (option to test 12 in)
- **Motor target:** ~140–160 kV outrunner on 12S
- **ESC:** 60–80 A, 12S rated
- **Climb target:** 400 fpm (~2.0 m/s)

### Climb Performance
- Time to 400 ft AGL: ~40–80 s
- Energy cost: < 10 Wh (negligible vs capacity)

---

## 11. Control & Modes (Conceptual)

### SOAR
- 28 mph IAS
- 0° sweep
- Minimal power

### DASH
- 45 mph IAS
- 45° sweep
- Moderate power for wind penetration

### FUTURE / AUTO
- Differential finger sweep for:
  - Yaw assist
  - Roll authority near stall
  - Braking / descent control

---

## 12. Design Philosophy

- Geometry over brute force
- Conservative speed margins
- Structural simplicity with aerodynamic subtlety
- Inspired by condor flight mechanics, not literal biomimicry

---

*This document captures the current design intent and assumptions for continued CAD, structural, and control-system development.*
