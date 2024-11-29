import pandas as pd
import numpy as np

arrays = [
    ['state A', 'state A', 'state B', 'state B'],
    ['City X', 'City Y', 'City X', 'City Y']
]
index = pd.MultiIndex.from_arrays(arrays, names=['state', 'City'])

data = {
    'Population': [4000, 5000, 6000, 7000],
    'GDP': [40000, 50000, 55000, 60000]
}

df = pd.DataFrame(data, index=index)

print("Original Multi-Index DataFrame:")
print(df)

print("\nData for 'state A':")
print(df.loc['state A'])

df['GDP per capita'] = df['GDP'] / df['Population']

print("\nDataFrame with GDP per capita:")
print(df)

grouped = df.groupby(level='state').sum()

print("\nTotal Population and GDP per Region:")
print(grouped)


swapped = df.swaplevel()
print("\nDataFrame with Swapped Levels:")
print(swapped)

sorted_df = df.sort_index()
print("\nDataFrame Sorted by MultiIndex:")
print(sorted_df)


print("\nData for 'City X' across all Regions:")
print(df.xs('City X', level='City'))
