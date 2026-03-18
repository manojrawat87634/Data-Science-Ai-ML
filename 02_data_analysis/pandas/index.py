import pandas as pd

data = {
    "name" : ["Manoj Rawat", "Redima Sharma"], 
    "age" : [21, 22]
}

df = pd.DataFrame(data)
print(df)

ds = pd.Series(["manoj", "Redima"])
print(ds)