import_sqlite3

def getData():
    # this variable lets us send and receive data back and forth from
    # our file to our database
    connect = _sqlite3.connect("testDb_p2.db")
    cursor = connect.cursor()

    query1 = "SELECT model FROM computers"
    query2 = "SELECT color FROM computers"

    # this is telling the program to fetch the query above
    cursor.execute(query1)

    cursor.fetchall()

    # storing the fetched data inside of results
    results = cursor.execute(query)

    # printing out data
    print(results)

getData()

def getSingleData():
    computerSearch = input("What computer are you looking for? Please type an ID number.")
    connect = _sqlite3.connect("testDb_p2.db")

    cursor = connect.cursor()

    query1 = f"SELECT model FROM computers WHERE id = {computerSearch}"

    # this is telling the program to fetch the query from above
    cursor.execute(query1)

    # storing the fetched data inside of results
    results = cursor.fetchpne()

    # printing out data
    print(results)

getSingleData()