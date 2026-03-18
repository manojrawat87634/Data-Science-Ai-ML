import pandas as pd
df = pd.read_csv('test.itinventories.csv')

print(df.size)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.values)
print(df.ndim)
print(df.T)
print(df.empty)
print(df.axes)
# print(df.tail())
