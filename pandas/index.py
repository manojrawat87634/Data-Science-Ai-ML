
import pandas as pd

df = pd.DataFrame({
    "name": ["manoj", "redima", "rawat", "sharma", "rahul", "priya", "amit", "neha", "vikas", "pooja"],
    
    "email": [
        "manoj@gmail.com",
        "redima@yahoo.com",
        "rawat@outlook.com",
        "sharma@gmail.com",
        "rahul@gmail.com",
        "priya@yahoo.com",
        "amit@outlook.com",
        "neha@gmail.com",
        "vikas@yahoo.com",
        "pooja@gmail.com"
    ],
    
    "age": [22, 25, 21, 28, 24, 23, 26, 22, 29, 20],
    
    "city": ["Delhi", "Mumbai", "Jaipur", "Delhi", "Pune", "Bhopal", "Indore", "Noida", "Gurgaon", "Agra"],
    
    "salary": [30000, 42000, 28000, 50000, 35000, 32000, 41000, 30000, 55000, 27000]
    
}, index=['a','b','c','d','e','f','g','h','i','j'])

# print(len(["manoj", "redima", "rawat", "sharma", "rahul", "priya", "amit", "neha", "vikas", "pooja"]))
# print(len( [
#         "manoj@gmail.com",
#         "redima@yahoo.com",
#         "rawat@outlook.com",
#         "sharma@gmail.com",
#         "rahul@gmail.com",
#         "priya@yahoo.com",
#         "amit@outlook.com",
#         "neha@gmail.com",
#         "vikas@yahoo.com",
#         "pooja@gmail.com"
#     ],
# ))
# print(len( [22, 25, 21, 28, 24, 23, 26, 22, 29, 20]))
# print(len(["Delhi", "Mumbai", "Jaipur", "Delhi", "Pune", "Bhopal", "Indore", "Noida", "Gurgaon", "Agra"]))
# print(len([30000, 42000, 28000, 50000, 35000, 32000, 41000, 30000, 55000, 27000]))

df.to_excel("r.xlsx")

data = pd.read_excel("r.xlsx")
# print(data.tail())
# print(data.head())
# print(data.describe())
# print(data.info())
# print(data.shape)
# print(data.dtypes)
# print(data.columns)


print(data.loc[1, "name"])
print(data.loc[[1, 2], ["name", 'email']])
df.loc[df['salary'] > 40000] 
total_salary = df["salary"].sum()
print(total_salary)
avg_age = df["age"].mean()
print(avg_age)
avg_age = df["age"].mean()
print(avg_age)
oldest_age = df["age"].max()
highest_salary = df["salary"].max()
num_names = df["name"].count()
df.groupby("city")["salary"].mean()


df.iloc[0]                      # First row
df.iloc[0, 2]                   # First row, third column
df.iloc[0:5]                    # First 5 rows
df.iloc[:, 1]   

data = pd.read_excel("r.xlsx", index_col=0)
json_data = data.to_json(orient="records", indent=4)
print(json_data)


print(df.groupby("city")["salary"].mean())

# print(data)
# for i, row in data.iterrows():
#     print(row)