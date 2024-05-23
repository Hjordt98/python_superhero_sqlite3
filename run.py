#!/usr/bin/env python
# coding: utf-8

# # 1 Database initialization and table creation

# In[15]:


import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('superheroes.db')
cur = con.cursor()

# Check if the table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='superheroes'")
if cur.fetchone() is None:
    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE superheroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            release_date INTEGER NOT NULL,
            hero_name TEXT NOT NULL,
            powers TEXT NOT NULL
        )
    """)
    con.commit()
    print("Table created.")    
else:
    cur.execute("""
        DROP TABLE superheroes        
                """)
    cur.execute("""
        CREATE TABLE superheroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            release_date INTEGER NOT NULL,
            hero_name TEXT NOT NULL,
            powers TEXT NOT NULL
        )
    """)
    print("Table already exists.")


# # 2 - insert data to tables

# In[16]:


# Insert data into the superheroes table
cur.execute("""
    INSERT INTO superheroes (first_name, last_name, release_date, hero_name, powers)
    VALUES (?, ?, ?, ?, ?)
""", ('Clark', 'Kent', 1938, 'Superman', 'Super strength, flight, x-ray vision'))

# Commit the changes
con.commit()

print("Data inserted successfully.")


# # 3 - data retrieval

# In[17]:


# Retrieve data from the superheroes table
cur.execute('SELECT * FROM superheroes')
rows = cur.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the connection
con.close()

