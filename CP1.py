import pandas as pd
import json
df_csv = pd.read_csv('data/researchers.csv')
df_active1_sorted=(((df_csv[(df_csv['is_active'] == True)&\
          (df_csv['h_index'] > 15)]).sort_values\
            ('joined_year', ascending=True))\
                ['last_name']).str[0]

print(df_active1_sorted)
clean_data = ""
for i in range(14):
    clean_data += df_active1_sorted.iloc[i]
print(clean_data)
    