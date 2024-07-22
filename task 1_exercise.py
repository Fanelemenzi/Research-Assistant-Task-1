# %%
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

count_share = pd.read_csv('F:\Coding Projects\RSA\count_share.csv')
value_share = pd.read_csv('F:\Coding Projects\RSA\import_value_share.csv')

# %%
comb_dataset = pd.concat([count_share, value_share], axis=1)
print(comb_dataset)

# %%
merge_dataset = pd.merge(count_share, value_share, on=['Year', 'CurrencyCode'], how='right')
print(merge_dataset)

# %%
final_dataset = merge_dataset.drop(columns=['Frequency_x','CumulativePercent_x','Frequency_y', 'CumulativePercent_y'])
print(final_dataset)

# %%
final_dataset.to_csv('task1_dataset.csv', index=False)


