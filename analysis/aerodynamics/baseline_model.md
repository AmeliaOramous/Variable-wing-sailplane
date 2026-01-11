# Baseline Aerodynamic Model (First-Order)

This model is intentionally simple.
It exists to compare configurations, not to predict final performance.

## Assumptions
- Subsonic, low-speed sailplane regime
- Quasi-steady aerodynamics
- Small angles (except where CLmax is invoked)
- No compressibility modeling
- No aeroelastic effects
- Sweep changes effective lift slope and induced drag primarily through geometry/effective span
- Profile drag handled via a basic parabolic polar

## Definitions
Let:
- W = weight
- rho = air density
- V = true airspeed
- q = 0.5 * rho * V^2
- S = planform area (held constant across sweep in concept diagrams)
- b = span (may change with sweep if geometry effectively shortens projected span)
- AR = b^2 / S
- e = Oswald efficiency factor (0.75–0.95 typical; treat as a knob)
- CL = W / (q * S)

## Drag Model (Parabolic Polar)
CD = CD0 + k * CL^2
where:
k = 1 / (pi * e * AR)

This separates:
- CD0 : profile + interference + misc (treat as a knob)
- induced drag : k * CL^2

## Key Outputs
- Lift coefficient required at speed:
  CL(V) = W / (0.5 * rho * V^2 * S)

- Drag:
  D(V) = q * S * CD(V)

- Glide ratio:
  L/D = CL / CD

- Sink rate (still-air):
  V_sink = V * (D / W)

## What Sweep Changes (in this simplified model)
Sweep affects performance mainly through:
1) Effective span (projected span) -> AR -> induced drag term k
2) Potential changes in CD0 (wetted area/flow separation risk) -> CD0 knob
3) Potential CLmax reduction at high sweep -> stall boundary shifts

This model treats these as parameter changes, not as detailed physics.

## Minimal Parameter Set Per Configuration
For each sweep state (min / max), define:
- S (m^2) — same unless you explicitly vary it
- b_eff (m) — projected or effective span
- e (—)
- CD0 (—)
- CLmax (—)

That is enough to make credible comparative plots.

## Sanity Checks
- As V increases, CL decreases ~ 1/V^2
- Induced drag dominates at low speed, profile drag dominates at high speed
- L/D has a single broad peak
