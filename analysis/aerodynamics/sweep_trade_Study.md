# Sweep Trade Study (First-Order)

Goal:
Compare min sweep vs max sweep across speed to understand *why* sweep helps,
and identify a reasonable conceptual sweep schedule.

## Inputs (fill these)
Common:
- W =
- rho =
- S =

Min sweep:
- b_eff_min =
- e_min =
- CD0_min =
- CLmax_min =

Max sweep:
- b_eff_max =
- e_max =
- CD0_max =
- CLmax_max =

## Method
For a range of V:
1) Compute CL(V) = W / (0.5 * rho * V^2 * S)
2) Compute CD(V) = CD0 + (1 / (pi * e * AR)) * CL^2
3) Compute L/D(V) and sink rate V_sink(V)
4) Enforce stall boundary: CL(V) <= CLmax
   - if CL required exceeds CLmax, that speed is not feasible

## Compare
- L/D vs V (both sweep states)
- Sink rate vs V (both sweep states)
- Feasible speed range (stall-limited) for each sweep state

## Interpretation Rules
- Min sweep should win at low speed (lower stall speed, higher induced efficiency)
- Max sweep should win at higher speed if:
  - effective AR penalty is acceptable AND/OR
  - CD0 is reduced or stays flat AND/OR
  - profile drag dominates and max sweep delays drag rise

## Output (what to put in diagrams)
- A conceptual sweep schedule: low speed -> min sweep, high speed -> max sweep
- The crossover speed where the curves intersect (conceptual, not final)

## Guardrails
- Do not publish absolute performance numbers unless backed by better modeling
- Do not tune parameters to “make it look good”
- If max sweep always loses, that’s not a failure—it's a design signal
