"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1
def k_imbalance(x):
    return (2*x)**2 / ((a - x)*(b - x)) - K

# TODO 2: Newton (root-finding)
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3: SLSQP on the squared imbalance
res = minimize(lambda v: k_imbalance(v[0])**2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print(f"Newton x = {x_newton:.6f}")
print(f"SLSQP  x = {x_slsqp:.6f}")
print("Agree:", np.isclose(x_newton, x_slsqp, atol=1e-4))

# TODO 4: composition and plot
x_eq = x_newton
H2, I2, HI = a - x_eq, b - x_eq, 2*x_eq
print(f"Equilibrium: H2 = {H2:.4f} mol, I2 = {I2:.4f} mol, HI = {HI:.4f} mol")
print(f"Check K = {HI**2/(H2*I2):.3f}")

xs = np.linspace(0, 0.999, 300)
plt.figure(figsize=(7, 4.5))
plt.plot(xs, a - xs, label="H2")
plt.plot(xs, b - xs, "--", label="I2")
plt.plot(xs, 2*xs, label="HI")
plt.axvline(x_eq, color="k", ls=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("extent x (mol)"); plt.ylabel("amount (mol)")
plt.title("H2 + I2 <=> 2 HI"); plt.legend(); plt.tight_layout()
plt.savefig("equilibrium.png", dpi=150)
