import pandas as pd
import json

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

#==========================================================
df_q31 = df_clean.groupby('researcher_id')['citations'].sum().idxmax()
print(df_q31)
top_researcher = df_clean[df_clean['researcher_id'] == df_q31][['first_name', 'last_name']].iloc[0]
print('\ntop_researcher is:')
print(top_researcher)

#==========================================================
df_q32 = df_clean.groupby('field')['amount_cad'].sum().idxmax()
print('\nfield with the most funding is:')
print(df_q32)

#==========================================================
df_clean['joined_year'] = pd.to_numeric(df_clean['joined_year'], errors='coerce')
df_q33_1 = df_clean[df_clean['is_active'] == True]
df_min_year = df_q33_1['joined_year'].min()
df_q33_2 = df_q33_1[df_q33_1['joined_year'] == df_min_year].iloc[0]

print('\nResearcher with the earliest join year and is still active is:')
print(df_q33_2[['first_name', 'last_name', 'joined_year']])