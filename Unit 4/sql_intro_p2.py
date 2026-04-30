# 1. import sqlite moddule to be able to use a database
import sqlite3

# 2. the connect method starts our database
connection = sqlite3.connect("testDb_p2.db")

# 3. this cursor variable creates a new object that let's us send objects to our database
cursor = connection.cursor()

# 4. We need to create a schema (structure) for our data
# cursor.execute('''
#     CREATE TABLE computer(
#     id INTEGER PRIMARY KEY,
#     model TEXT,
#     color TEXT,
#     hasWebcam BOOL,
#     memory INTEGER,
#     price INTEGER                                                               
#                )''')

cursor.execute('''
    INSERT INTO computer(model, color, hasWebcam, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)
               ''')

# CREATE A COMPUTER
cursor.execute('''
    INSERT INTO computer(model, color, hasWebcam, memory, price)
    VALUES('Asus', 'black', False, 16, 1300)''')

connection.commit()

connection.close()

# UPDATE A COMPUTER
cursor.execute('''
    UPDATE computer
    SET price = 3000
    SET color = 'orange'
    WHERE id = 2
               ''')

# CREATE A COMPUTER
cursor.execute('''
    UPDATE computer
    SET price = 1000
    SET color = 'red'
    WHERE id = 1
               ''')
    
# CREATE A COMPUTER
cursor.execute('''
    UPDATE computer
    SET price = 2030
    SET color = 'purple'
    WHERE id = 3
               ''')