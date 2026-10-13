import pandas as pd

df = pd.read_csv("heart.csv")

print("Shape:", df.shape)
print(df.head())

cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.describe())

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, col in zip(axes.flatten(), cont.columns):
    ax.hist(cont[col], bins=20, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("count")

plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.show()