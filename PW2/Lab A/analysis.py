"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", a.mean())
print("Std of acceleration:", a.std())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
print("Max position difference:", np.max(np.abs(y_rec - y)))

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axs[0].plot(t, y)
axs[0].set_ylabel("Position (m)")

axs[1].plot(t, v)
axs[1].set_ylabel("Velocity (m/s)")

axs[2].plot(t, a)
axs[2].axhline(-9.81, linestyle="--", color="red", label="-9.81")
axs[2].set_ylabel("Acceleration (m/s²)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()

fig.tight_layout()
plt.savefig("motion.png")

# ---------- Bonus: 2D tracked trajectory ----------
traj = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
tt = traj[:, 0]
x = traj[:, 1]
yy = traj[:, 2]

vx = np.gradient(x, tt)
vy = np.gradient(yy, tt)
speed = np.sqrt(vx**2 + vy**2)
print("Mean speed:", speed.mean())

fig2, axs2 = plt.subplots(1, 2, figsize=(11, 4))

axs2[0].plot(x, yy)
axs2[0].set_xlabel("x (m)")
axs2[0].set_ylabel("y (m)")
axs2[0].set_title("Path")
axs2[0].set_aspect("equal")

axs2[1].plot(tt, speed)
axs2[1].set_xlabel("Time (s)")
axs2[1].set_ylabel("Speed (m/s)")
axs2[1].set_title("Speed")

fig2.tight_layout()
fig2.savefig("trajectory.png")