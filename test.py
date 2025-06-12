print("Hello, I’m ready!")
import matplotlib
import seaborn
import streamlit
print("All libraries are ready!")

import sqlite3

# Connect to a new database (it’ll create a file called test.db)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a tiny table for toys
cursor.execute('''
    CREATE TABLE IF NOT EXISTS toys (
        toy_name TEXT,
        price REAL
    )
''')

# Add a toy
cursor.execute("INSERT INTO toys (toy_name, price) VALUES ('Teddy Bear', 50.0)")

# Save the changes
conn.commit()

# Check if the toy is there
cursor.execute("SELECT * FROM toys")
result = cursor.fetchall()
print("My toys:", result)

# Close the database
conn.close()
