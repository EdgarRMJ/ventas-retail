import pandas as pd

df = pd.read_csv('data/SampleSuperstore.csv', encoding='latin-1')
pd.set_option('display.max_columns', None)
print(df.head())
print(df.head())
print(df.columns)
print(df.info())