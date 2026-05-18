import pandas as pd
import json
#==============================================================
# read csv file

df_csv = pd.read_csv('data/researchers.csv')

df_csv.shape
print(df_csv.head(10))
df_csv.dtypes
df_csv.isnull().sum()
df_csv.describe()
df_csv.info()



#==========================================================
# read json file

# flat JSON → DataFrame
df_json1 = pd.read_json('data/publications.json')
# nested JSON → use json + normalize
data_json = json.load(open('data/publications.json'))
df_json_norm = pd.json_normalize(data_json)


#==========================================================
# read excel file

df_excel = pd.read_excel('data/funding.xlsx')

