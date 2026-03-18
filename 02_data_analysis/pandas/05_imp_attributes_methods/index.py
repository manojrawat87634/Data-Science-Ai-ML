import pandas as pd
import numpy as np
df = pd.read_csv('test.itinventories.csv')

# df = pd.DataFrame({
#     "name" : ["Manoj Rawat", "Redima Sharma"],
#     "age" : [21, 23]
# })

# print(df.size)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.values)
# print(df.ndim)
# print(df.T)
# print(df.empty)
# print(df.axes)

# print(df.tail())
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.sample())
# print(df.loc[ :,"_id"])
# print(df.iloc[0, 1])
# print(df.at[ 1,"_id"])
# print(df.iat[ 2,1])


# print(df.query("serialNo < 2"))
# df_dropped = df.dropna()
# print(df["_id"].isin(["6978867e4c5487460661c421"]))


# Sample data
df = pd.DataFrame({
    "Name": ["A", "B", None, "D"],
    "Age": [20, np.nan, 22, 23],
    "City": ["Delhi", "Mumbai", "Delhi", None]
})

print("Original Data:\n", df)


# 1. Detect missing
print("\nMissing Values:\n", df.isnull())

# 2. Fill missing
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(0)
df["City"] = df["City"].fillna("Unknown")

# 3. Replace values
df = df.replace("Delhi", "New Delhi")

# 4. Rename column
df = df.rename(columns={"Name": "FullName"})

# 5. Change datatype
df["Age"] = df["Age"].astype(int)

# 6. Drop column
df = df.drop("City", axis=1)

# 7. Sort values
df = df.sort_values(by="Age")

print("\nCleaned Data:\n", df)
