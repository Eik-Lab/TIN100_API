import sqlite3 # Biblioteket vi skal bruke for å kommunisere med sqlite-databasen
from sqlite3 import Error

connection = sqlite3.connect("database.db") # 

if connection is not None: # Sjekker om opprettelsen av databasen var en suksess
    sql_create_table =  "CREATE TABLE IF NOT EXISTS sensordata (id integer PRIMARY KEY, value real NOT NULL); "
    try:
        c = connection.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)



connection.close() # Viktig å lukke databasen før programmet avslutter