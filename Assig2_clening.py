import pandas as pd
import json

df_researchers = pd.read_csv('data/researchers.csv')
df_funding = pd.read_excel('data/funding.xlsx')
df_publications = pd.read_json('data/publications.json')
#==========================================================

df_merged2 = pd.merge(df_researchers, df_publications,\
                      on='researcher_id', how='left')
df_merged_left = pd.merge(df_merged2, df_funding,\
                      on='researcher_id', how='left')

df_merged_left['amount_cad'] = pd.to_numeric\
    (df_merged_left['amount_cad'],errors='coerce')
df_clean = df_merged_left[(df_merged_left['amount_cad'] > 0)&\
        (df_merged_left['amount_cad'].notnull())]
