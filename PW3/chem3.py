import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")

sub = df[(df["pollution_index"] > 40) & (df["pollution_index"] < 60)]
print("patients in the band 40 < pollution_index < 60:", len(sub))

print()
for chem in ["benzene", "cadmium"]:
    r_all, _ = stats.pearsonr(df[chem], df["malignancy"])
    r_sub, p_sub = stats.pearsonr(sub[chem], sub["malignancy"])
    print(f"{chem:8s} all patients: r = {r_all:6.3f}   restricted: r = {r_sub:6.3f} (p = {p_sub:.2e})")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(sub[chem], sub["malignancy"], alpha=0.5, s=14)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")
    ax.set_title(chem + " (pollution_index 40-60)")

plt.tight_layout()
plt.savefig("controlled.png", dpi=150)
plt.show()