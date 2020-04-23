import os
import sqlite3
import pandas as pd

data = pd.read_csv('Film_Database.csv')
print(data.head())

# Clear the database if it exists
if os.path.exists('Film.db'):
    os.remove('Film.db')

# Create a connection to the database
conn = sqlite3.connect('Film.db')

# Add the data to the database
data.to_sql('data', conn, dtype={
    'Title': 'TEXT',
    'Release_Year': 'INTEGER',
    'Mood': 'TEXT',
    'Genre': 'TEXT',
    'Type': 'Text',
    'Length': 'Text'
})

conn.row_factory = sqlite3.Row # allows name-based access to columns

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows