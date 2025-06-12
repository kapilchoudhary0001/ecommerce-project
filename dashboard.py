import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title('My Toy Store Dashboard 🎲')

st.write('Hi! I analyzed toy sales to find the best toys and customers!')

# Load top toys chart
conn = sqlite3.connect('toys.db')
df = pd.read_sql_query('''
    SELECT ToyName, SUM(Quantity * Price) as TotalMoney
    FROM toy_sales
    GROUP BY ToyName
    ORDER BY TotalMoney DESC
    LIMIT 5
''', conn)
conn.close()

st.subheader('Top 5 Toys by Sales')
fig, ax = plt.subplots()
ax.bar(df['ToyName'], df['TotalMoney'], color='skyblue')
ax.set_title('Top 5 Toys by Sales')
ax.set_xlabel('Toy Name')
ax.set_ylabel('Total Money (₹)')
plt.xticks(rotation=45)
st.pyplot(fig)

st.write('These are the toys everyone loves!')
st.subheader('Who Are My Best Customers?')
conn = sqlite3.connect('toys.db')
df_customers = pd.read_sql_query('''
    SELECT CustomerID, 
           COUNT(DISTINCT InvoiceNo) as HowOften, 
           SUM(Quantity * Price) as TotalSpent
    FROM toy_sales
    GROUP BY CustomerID
''', conn)
conn.close()

fig, ax = plt.subplots()
ax.scatter(df_customers['HowOften'], df_customers['TotalSpent'], color='purple')
ax.set_title('Customers: How Often vs. How Much They Spend')
ax.set_xlabel('Number of Purchases')
ax.set_ylabel('Total Spent (₹)')
for i, txt in enumerate(df_customers['CustomerID']):
    ax.annotate(txt, (df_customers['HowOften'][i], df_customers['TotalSpent'][i]))
st.pyplot(fig)
# Sales over time line chart
st.subheader('Toy Sales Over Time')
conn = sqlite3.connect('toys.db')
df_time = pd.read_sql_query('''
    SELECT InvoiceDate, SUM(Quantity * Price) as TotalMoney
    FROM toy_sales
    GROUP BY InvoiceDate
''', conn)
conn.close()

fig, ax = plt.subplots()
ax.plot(df_time['InvoiceDate'], df_time['TotalMoney'], marker='o', color='green')
ax.set_title('Toy Sales Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Total Money (₹)')
plt.xticks(rotation=45)
st.pyplot(fig)