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