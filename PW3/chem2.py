import pandas as pd

df = pd.read_csv("chemicals_cancer.csv")

print(df.corr().round(2))