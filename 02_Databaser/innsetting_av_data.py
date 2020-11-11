import sqlite3 
from sqlite3 import Error 

import random

connection = sqlite3.connect("database.db")

sql_insert = "INSERT INTO sensordata (value) VALUES (0.7)"

c = connection.cursor()
c.execute(sql_insert)

for i in range(9):
    sql_insert = f'INSERT INTO sensordata (value) VALUES ({round(random.random(), 2)})'
    c.execute(sql_insert)

connection.commit()
connection.close()