# %%
import pandas as pd
import json
#==============================================================
# read csv file

df_csv = pd.read_csv('data/researchers.csv')

# print(df_csv.shape)
#%%
# print(df_csv.head(10))
# print(df_csv.dtypes)
# print("Missing values in each column:")
# print(df_csv.isnull().sum())
# print("Unique values in each column:")
# print(df_csv.describe())
# print(df_csv.info())
# print("groupby field and calculate mean h_index:")
# df_group = df_csv.groupby('field')['h_index'].mean()
# print(df_group)
# # print(df_group)
#%%
# df_active= df_csv[df_csv['is_active'] == True]
# df_active= df_csv[df_csv['is_active'] == True]\
# .groupby('institution')['researcher_id'].count()

# print("Active researchers:")
# print(df_active)
# df_agg = df_csv.groupby('field').agg({'h_index': ['mean', 'max'], 'publications_count': 'sum'})
# print("multiple aggregation:")
# print(df_agg)

# print(df_agg.sort_values(('h_index', 'mean'), ascending=False))

df_active1_sorted=(((df_csv[(df_csv['is_active'] == True)&\
          (df_csv['h_index'] > 15)]).sort_values\
            ('joined_year', ascending=True))\
                ['last_name']).str[0]

print(df_active1_sorted)




#==========================================================
# read json file

# # flat JSON → DataFrame
# df_json1 = pd.read_json('data/publications.json')
# # nested JSON → use json + normalize
# data_json = json.load(open('data/publications.json'))
# df_json_norm = pd.json_normalize(data_json)


# #==========================================================
# # read excel file

# df_excel = pd.read_excel('data/funding.xlsx')


# %%
