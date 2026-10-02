"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).
Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read data
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t, C = data[:, 0], data[:, 1]
C0 = C[0]

# TODO 2: total error
def total_error(k):
    k = np.ravel(k)[0]          # minimize passes an array
    return np.sum((C - C0*np.exp(-k*t))**2)

# TODO 3: minimise
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print(f"Fitted rate constant k = {k_fit:.4f}")
print(f"C0 = {C0:.3f}, total error = {res.fun:.3f}")

# TODO 4: plot
tt = np.linspace(t.min(), t.max(), 300)
plt.figure(figsize=(7, 4.5))
plt.plot(t, C, "o", label="measured")
plt.plot(tt, C0*np.exp(-k_fit*tt), "-", label=f"fit: k = {k_fit:.3f}")
plt.xlabel("time"); plt.ylabel("concentration")
plt.title("First-order decay fit"); plt.legend(); plt.tight_layout()
plt.savefig("kinetics.png", dpi=150)
