import math
import csv

# ---- Fill these ----
W = 3000.0          # N
rho = 1.225         # kg/m^3
S = 12.0            # m^2

configs = {
    "min": {
        "b_eff": 18.0,      # m
        "e": 0.90,          # -
        "CD0": 0.018,       # -
        "CLmax": 1.4,       # -
    },
    "max": {
        "b_eff": 14.0,      # m
        "e": 0.85,          # -
        "CD0": 0.018,       # -
        "CLmax": 1.2,       # -
    },
}

V_list = [v for v in range(12, 61, 1)]  # m/s

def compute_row(cfg, V):
    q = 0.5 * rho * V * V
    CL = W / (q * S)

    AR = (cfg["b_eff"] ** 2) / S
    k = 1.0 / (math.pi * cfg["e"] * AR)

    CD = cfg["CD0"] + k * CL * CL
    LD = CL / CD

    D = q * S * CD
    sink = V * (D / W)

    stall_limited = CL > cfg["CLmax"]
    return CL, CD, LD, sink, stall_limited

out_path = "analysis/aerodynamics/polar_filled.csv"
with open(out_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["config", "V_mps", "CL", "CD", "LD", "sink_mps", "stall_limited"])
    for name, cfg in configs.items():
        for V in V_list:
            CL, CD, LD, sink, stall = compute_row(cfg, V)
            w.writerow([name, V, round(CL, 4), round(CD, 5), round(LD, 2), round(sink, 3), stall])

print(f"Wrote {out_path}")
