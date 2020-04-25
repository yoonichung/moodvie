import os
import sqlite3
import pandas as pd

data = pd.read_csv('functions/Film_Database.csv')

# Clear the database if it exists
if os.path.exists('film.db'):
    os.remove('film.db')

# Create a connection to the database
conn = sqlite3.connect('film.db')

# Add the data to the database
data.to_sql('data', conn)

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    cols = cur.description
    rows = cur.fetchall()
    return rows

def sql_query_conditional(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

