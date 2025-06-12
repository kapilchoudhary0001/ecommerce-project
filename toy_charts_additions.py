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