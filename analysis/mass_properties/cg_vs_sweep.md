# CG vs Sweep (Conceptual)

Goal:
Understand whether sweeping the wing changes CG enough to matter.

## Assumptions
- Wing mass is not negligible
- Sweep rotates wing mass about a pivot axis near the root
- Fuselage mass distribution remains fixed
- No fuel shift (sailplane)

## Minimal Model
Let:
- m_fuse, x_fuse : fuselage + payload lumped mass and CG position
- m_wing : total wing mass
- r_w : distance from pivot axis to wing mass centroid (in plan view)
- theta : sweep angle (0 at min sweep)
- x_pivot : pivot location along fuselage axis

Wing mass centroid x-position (conceptual):
x_w(theta) = x_pivot + r_w * sin(theta)

Total CG:
x_CG(theta) = (m_fuse * x_fuse + m_wing * x_w(theta)) / (m_fuse + m_wing)

## What to Look For
- Does x_CG shift exceed your allowable CG range?
- Does CG shift direction match intuition? (increased sweep tends to move wing mass aft)

## Output
- A simple plot: x_CG vs theta
- A single statement: “CG shift is small / moderate / dominant”
