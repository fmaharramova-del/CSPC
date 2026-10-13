import numpy as np
import pandas as pd

df = pd.read_csv("heart.csv")

for col in ["target", "sex"]:
    p = df[col].value_counts(normalize=True)
    entropy = -(p * np.log2(p)).sum()
    max_entropy = np.log2(len(p))
    print(col)
    print(p.round(3).to_string())
    print(f"entropy = {entropy:.3f} bits (maximum possible = {max_entropy:.3f})")
    print(f"guessing the most common class is right {p.max():.1%} of the time")
    print()