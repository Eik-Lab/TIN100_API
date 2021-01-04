import sqlite3 
from sqlite3 import Error 

import random

connection = sqlite3.connect("database.db") # Kobler til databasen vi opprettet i 1_lage_database.py

sql_insert = "INSERT INTO sensordata (value) VALUES (0.9)" # Eksempel på kommando for å sette inn data

c = connection.cursor()
c.execute(sql_insert) # Utfører kommanoen
connection.commit()


# Setter inn flere rader med en for-løkke
for i in range(9):
    sql_insert = f'INSERT INTO sensordata (value) VALUES ({round(random.random(), 2)})'
    c.execute(sql_insert)

connection.commit()
connection.close()