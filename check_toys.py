import sqlite3

# Connect to the database
conn = sqlite3.connect('toys.db')
cursor = conn.cursor()

# Look at the first 5 rows
cursor.execute("SELECT * FROM toy_sales LIMIT 5")
results = cursor.fetchall()
print("First 5 toy sales:")
for row in results:
    print(row)

conn.close()
