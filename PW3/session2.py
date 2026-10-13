import pandas as pd
from scipy import stats

df = pd.read_csv("heart.csv")

disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]

print("disease: n =", len(disease), " mean =", round(disease.mean(), 2), " median =", disease.median())
print("healthy: n =", len(healthy), " mean =", round(healthy.mean(), 2), " median =", healthy.median())

u, p = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print("Mann-Whitney U =", u)
print("p-value =", p)

import matplotlib.pyplot as plt

mean_d, sem_d = disease.mean(), stats.sem(disease)
mean_h, sem_h = healthy.mean(), stats.sem(healthy)

print("disease: mean =", round(mean_d, 2), " SEM =", round(sem_d, 2))
print("healthy: mean =", round(mean_h, 2), " SEM =", round(sem_h, 2))

plt.figure(figsize=(5, 5))
plt.errorbar([0, 1], [mean_d, mean_h], yerr=[sem_d, sem_h],
             fmt="o", capsize=8, markersize=8)
plt.xticks([0, 1], ["disease", "healthy"])
plt.xlim(-0.5, 1.5)
plt.ylabel("max heart rate (thalach), mean ± SEM")
plt.title("Mean thalach by group")
plt.tight_layout()
plt.savefig("thalach_means.png", dpi=150)
plt.show()