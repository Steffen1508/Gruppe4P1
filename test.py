import pandas as pd

df = pd.read_parquet("hf://datasets/syvai/pii-dataset-eng/data/train-00000-of-00001.parquet")
print(df.head())
print("Antal rækker:",len(df))
print("Antal klonner:", df.shape[1])
print(df.isnull().sum())   # --> Show Missing Value 
df.info()

