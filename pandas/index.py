import pandas as pd

data = pd.Series([12, 14, 16])

df = pd.DataFrame({
    "name" : ["abc", "xyz", "manoj"],
    "email" : ["abc@gmail.com", "xyz@gmail.com", "manoj@gmail.com"]
})

print(df)
print(data)