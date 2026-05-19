import pandas as pd
import json
import os

def clean_funding(df):

    df['amount_cad'] = pd.to_numeric(
        df['amount_cad'], errors='coerce')

    df_clean = df[(df['amount_cad'] > 0) &
                   (df['amount_cad'].notnull())]

    return df_clean

df_researchers = pd.read_csv('data/researchers.csv')
df_funding = pd.read_excel('data/funding.xlsx')
df_publications = pd.read_json('data/publications.json')
#==========================================================

df_merged2 = pd.merge(df_researchers, df_publications,                      on='researcher_id', how='left')
df_merged_left = pd.merge(df_merged2, df_funding,
                        on='researcher_id', how='left')


df_clean = clean_funding(df_merged_left)



os.makedirs("output", exist_ok=True)

df_clean.to_csv("output/clean_research_data.csv", index=False)