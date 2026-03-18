import pandas as pd

df = pd.read_csv("../01_file_handling/test.itinventories.csv")

print(df.head()["createdAt"])
df['createdAt'] = pd.to_datetime(df['createdAt'])
print(df.head()['createdAt'])
# print(pd.notnull(df))
# print(pd.isnull(df))