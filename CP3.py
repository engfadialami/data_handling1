import pandas as pd
import json

df = pd.read_excel('data/funding.xlsx')
df.shape
df.isnull().sum()
df['amount_cad'] = pd.to_numeric\
    (df['amount_cad'],errors='coerce')
df = df[df['amount_cad'] > 0]

df_clean_total = df[df['amount_cad'] > 0]['amount_cad'].sum()

