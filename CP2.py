import pandas as pd
import json

df_json = pd.read_json('data/publications.json')

# print(df_json.info())
# df_json.groupby('title').agg({'citations': 'max'}) 
# Max was not the right parameter, it should be sum,\
#  because we want to find the title with the most\
#  citations, not the maximum citations for each title.

# (df_json.groupby('title').\
#  agg({'citations': ['max','sum']}))

df_json.groupby('title')['citations'].sum().idxmax()

