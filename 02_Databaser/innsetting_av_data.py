import sqlite3 
from sqlite3 import Error 

connection = sqlite3.connect("database.db")

sql_insert = "INSERT INTO sensordata (value) VALUES (1)"

c = connection.cursor()
c.execute(sql_insert)
connection.commit()
connection.close()