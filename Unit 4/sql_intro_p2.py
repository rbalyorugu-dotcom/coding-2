# 1. import sqlite moddule to be able to use a database
import sqlite3

# 2. the connect method starts our database
connection = sqlite3.connect()

# 3. this cursor variable creates a new object that let's us send objects to our database
cursor = connect.cursor()

# 4. We need to create a schema (structure) for our data
cursor.execute('''
    CREATE TABLE computers(
    id INTEGER PRIMARY KEY,
    model TEXT,
    color TEXT,
    hasWebcam BOOL,
    memory INTEGER,
    price INTEGER,                                                               
               )''')

cursor.execute('''
    INSERT INTO computer(model, color, hasWebcam, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)''')

connect.comit()
connect.close()