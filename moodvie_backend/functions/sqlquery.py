import os
import sqlite3
import pandas as pd

data = pd.read_excel('functions/Film_Database.xls')
data.columns = data.columns.str.strip()

# Clear the database if it exists
if os.path.exists('film.db'):
    os.remove('film.db')

# Create a connection to the database
conn = sqlite3.connect('film.db')
cur = conn.cursor()

# Add the data to the database
data.to_sql('data', conn)

# to view all tables
def view_tables():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables =cur.fetchall()
    return tables

# Create recommendations database
def sql_make_rec():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS recommendations (ID INTEGER PRIMARY KEY, Film TEXT, Length TEXT, Movie_Type TEXT, Genre TEXT)")
    conn.commit()

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





