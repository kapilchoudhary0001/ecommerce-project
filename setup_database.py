import sqlite3
import pandas as pd

# Read your CSV file
df = pd.read_csv('toys.csv')

# Connect to a new database (creates toys.db)
conn = sqlite3.connect('toys.db')
cursor = conn.cursor()

# Create a table for toy sales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS toy_sales (
        InvoiceNo TEXT,
        ToyName TEXT,
        Quantity INTEGER,
        Price REAL,
        InvoiceDate TEXT,
        CustomerID TEXT
    )
''')

# Put the data into the table
df.to_sql('toy_sales', conn, if_exists='replace', index=False)

# Save and close
conn.commit()
conn.close()
print("Toy sales data loaded into toys.db!")
