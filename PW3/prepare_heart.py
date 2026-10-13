import pandas as pd

columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
           "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]

df = pd.read_csv("processed.cleveland.data", header=None,
                 names=columns, na_values="?")

df["target"] = (df["num"] > 0).astype(int)
df = df.drop(columns=["num"])

df.to_csv("heart.csv", index=False)

print("Shape:", df.shape)
print(df["target"].value_counts())
print("Пропуски по столбцам:")
print(df.isna().sum())