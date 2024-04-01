import sqlite3 as sql

connection = sql.connect('User.db')
cursor = connection.cursor()
result = cursor.fetchall()

connection.execute('''CREATE TABLE IF NOT EXISTS Users (Username VARCHAR(20), Password VARCHAR(20))''')

connection.execute('''INSERT INTO Users''')