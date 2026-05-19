import pandas as pd
import json

df_researchers = pd.read_csv('data/researchers.csv')
df_funding = pd.read_excel('data/funding.xlsx')
df_publications = pd.read_json('data/publications.json')
#==========================================================

df_merged1 = pd.merge(df_researchers, df_funding,\
                      on='researcher_id', how='inner')
df_merged_inner = pd.merge(df_merged1, df_publications,\
                      on='researcher_id', how='inner')
#==========================================================

df_merged2 = pd.merge(df_researchers, df_publications,\
                      on='researcher_id', how='left')
df_merged_left = pd.merge(df_merged2, df_funding,\
                      on='researcher_id', how='left')

# df_merged2_test = pd.merge(df_researchers, df_publications,\
#                       on='researcher_id', how='left', indicator='pub_merge')
# df_merged_left_test = pd.merge(df_merged2_test, df_funding,\
#                       on='researcher_id', how='left', indicator= 'funding_merge')

df_researchers.shape
df_funding.shape
df_publications.shape
df_merged_inner.shape
df_merged_left.shape

