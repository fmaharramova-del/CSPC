import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")

print("Shape:", df.shape)
print(df.head())
print(df.describe())

print()
for chem in ["benzene", "cadmium"]:
    r_p, p_p = stats.pearsonr(df[chem], df["malignancy"])
    r_s, p_s = stats.spearmanr(df[chem], df["malignancy"])
    print(f"{chem:8s} Pearson r = {r_p:6.3f} (p = {p_p:.2e})   Spearman rho = {r_s:6.3f} (p = {p_s:.2e})")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(df[chem], df["malignancy"], alpha=0.4, s=12)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")
    ax.set_title(chem + " vs malignancy")

plt.tight_layout()
plt.savefig("naive.png", dpi=150)
plt.show()