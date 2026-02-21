import sqlite3

conn = sqlite3.connect("data/lab_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM processed_data")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()