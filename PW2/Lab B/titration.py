"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V, pH = data[:, 0], data[:, 1]

# TODO 2
slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print(f"Equivalence point: V = {V_eq:.2f} mL (pH = {pH[i]:.2f}, slope = {slope[i]:.2f} pH/mL)")

# TODO 3
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
ax[0].plot(V, pH)
ax[0].axvline(V_eq, color="r", ls="--", label=f"equivalence {V_eq:.1f} mL")
ax[0].set_xlabel("volume of base (mL)"); ax[0].set_ylabel("pH")
ax[0].set_title("Titration curve"); ax[0].legend()
ax[1].plot(V, slope)
ax[1].axvline(V_eq, color="r", ls="--")
ax[1].set_xlabel("volume of base (mL)"); ax[1].set_ylabel("dpH/dV")
ax[1].set_title("Slope (peaks at equivalence)")
plt.tight_layout()
plt.savefig("titration.png", dpi=150)
