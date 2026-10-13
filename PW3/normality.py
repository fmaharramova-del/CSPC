import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")
cont = df[["age", "chol", "trestbps", "thalach"]]

print("variable    skew    Shapiro_W    p-value")
for col in cont.columns:
    x = cont[col]
    w, p = stats.shapiro(x)
    print(f"{col:9s} {stats.skew(x):7.2f} {w:10.4f} {p:12.2e}")

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flatten(), cont.columns):
    stats.probplot(cont[col], dist="norm", plot=ax)
    ax.set_title("Q-Q plot: " + col)

plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.show()