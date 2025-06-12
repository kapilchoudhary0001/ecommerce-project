import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Get data from SQLite
conn = sqlite3.connect('toys.db')
df = pd.read_sql_query('''
    SELECT ToyName, SUM(Quantity * Price) as TotalMoney
    FROM toy_sales
    GROUP BY ToyName
    ORDER BY TotalMoney DESC
    LIMIT 5
''', conn)
conn.close()

# Make a bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['ToyName'], df['TotalMoney'], color='skyblue')
plt.title('Top 5 Toys by Sales')
plt.xlabel('Toy Name')
plt.ylabel('Total Money (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_toys.png')  # Save the chart
plt.show()
# Get sales by date
conn = sqlite3.connect('toys.db')
df_time = pd.read_sql_query('''
    SELECT InvoiceDate, SUM(Quantity * Price) as TotalMoney
    FROM toy_sales
    GROUP BY InvoiceDate
''', conn)
conn.close()

# Make a line chart
plt.figure(figsize=(8, 5))
plt.plot(df_time['InvoiceDate'], df_time['TotalMoney'], marker='o', color='green')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Money (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_time.png')
plt.show()
# Get customer data
conn = sqlite3.connect('toys.db')
df_customers = pd.read_sql_query('''
    SELECT CustomerID, 
           COUNT(DISTINCT InvoiceNo) as HowOften, 
           SUM(Quantity * Price) as TotalSpent
    FROM toy_sales
    GROUP BY CustomerID
''', conn)
conn.close()

# Make a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df_customers['HowOften'], df_customers['TotalSpent'], color='purple')
plt.title('Customers: How Often vs. How Much They Spend')
plt.xlabel('Number of Purchases')
plt.ylabel('Total Spent (₹)')
for i, txt in enumerate(df_customers['CustomerID']):
    plt.annotate(txt, (df_customers['HowOften'][i], df_customers['TotalSpent'][i]))
plt.tight_layout()
plt.savefig('customer_groups.png')
plt.show()
