import sqlite3 
from sqlite3 import Error 

connection = sqlite3.connect("database.db")

print("----------- \n All data:")

sql_query = "SELECT * from sensordata"

c = connection.cursor()
c.execute(sql_query)

rows = c.fetchall()

for row in rows:
    print(row)


print("----------- \n Første 2 punkter i tabellen:")

sql_query = "SELECT * from sensordata LIMIT 2"

c.execute(sql_query)

rows = c.fetchall()

for row in rows:
    print(row)


connection.close()