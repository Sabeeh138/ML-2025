import pandas as pd

data1 = pd.read_csv('Lab2 D1A.csv')
data2 = pd.read_csv('Lab2 D1B.csv')
data3 = pd.read_csv('Lab2 D1C.csv')

print(data1.shape, data2.shape, data3.shape)
print(data1.head())
print(data2.head())
print(data3.head())

common_cols = list(data1.columns.intersection(data2.columns))

merged_AB = pd.merge(data1, data2, on=common_cols, how='outer')

print(merged_AB.shape)
print(merged_AB.columns)

common_cols_AC = list(data1.columns.intersection(data3.columns))

comboAC = pd.merge(data1, data3, on=common_cols_AC, how='inner')

print(comboAC.shape)
