import pandas as pd
import json

df_json = pd.read_json('data/publications.json')
df_json.shape
data_json = json.load(open('data/publications.json'))
df_json_norm = pd.json_normalize(data_json)
df_json_norm.shape

print(df_json_norm.groupby('title')['citations'].sum().idxmax())
