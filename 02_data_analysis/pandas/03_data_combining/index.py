import pandas as pd

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 21]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Age": [22, 23]
})

result = pd.concat([df1, df2])
print(result)
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [90, 80]
})

result = pd.merge(df1, df2, on="ID")
print(result)
