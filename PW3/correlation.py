import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

r_s, p_s = stats.spearmanr(df["age"], df["thalach"])
r_p, p_p = stats.pearsonr(df["age"], df["thalach"])

print("Spearman: rho =", round(r_s, 3), " p =", p_s)
print("Pearson:  r   =", round(r_p, 3), " p =", p_p)

plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach (max heart rate)")
plt.title("Age vs max heart rate")
plt.tight_layout()
plt.savefig("age_thalach.png", dpi=150)
plt.show()