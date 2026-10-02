"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

def gradient_descent(grad, x0, lr=0.01, tol=1e-10, max_iter=100000):
    """x = x - lr*grad(x) until the step is tiny."""
    x = x0
    for _ in range(max_iter):
        step = lr * grad(x)
        x = x - step
        if abs(step) < tol:
            break
    return x

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

print("=== 2A: f(x) = (x-3)^2 + 1, x0 = 0 ===")
print("Gradient descent:", gradient_descent(df, 0.0, lr=0.1))
print("Newton          :", newton(df, 0.0, fprime=d2f))
print("SLSQP           :", minimize(lambda v: f(v[0]), [0.0], method="SLSQP").x[0])

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in (0.0, 2.0):
    print(f"\n=== 2B: g(x) = x^4 - 3x^2 + x + 5, x0 = {x0} ===")
    xg = gradient_descent(dg, x0, lr=0.01)
    print(f"Gradient descent: x = {xg:.6f}, g = {g(xg):.6f}")

    xn = newton(dg, x0, fprime=d2g)
    kind = "MINIMUM" if d2g(xn) > 0 else "MAXIMUM"
    print(f"Newton          : x = {xn:.6f}, g = {g(xn):.6f}, "
          f"g'' = {d2g(xn):.3f} -> {kind}")

    xs = minimize(lambda v: g(v[0]), [x0], method="SLSQP").x[0]
    print(f"SLSQP           : x = {xs:.6f}, g = {g(xs):.6f}")
