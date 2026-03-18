import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)")

cursor.execute("INSERT INTO users VALUES (1, 'Manoj', 22)")
cursor.execute("INSERT INTO users VALUES (2, 'Rahul', 25)")

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()