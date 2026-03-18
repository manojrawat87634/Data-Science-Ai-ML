import pandas as pd
import sqlite3 
# df = pd.read_csv('test.itinventories.csv')
# df = pd.read_excel('test.itinventories.xlsx')
df = pd.read_json('faculties.json')

# conn = sqlite3.connect("test.db")
# df = pd.read_sql("select * from users", conn)
print(df.head())
# print(df.tail())