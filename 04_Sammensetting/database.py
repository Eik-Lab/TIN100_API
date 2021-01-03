import sqlite3
from sqlite3 import Error

import random, time


def open_database(db_navn):

    connection = sqlite3.connect(db_navn) # 


    if connection is not None:  # Sjekker om opprettelsen av databasen var en suksess
        sql_create_table = "CREATE TABLE IF NOT EXISTS sensordata (id integer PRIMARY KEY AUTOINCREMENT, value int, date int); "
    try:
        c = connection.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

    return connection

if __name__ == '__main__':
    db = open_database('sensordata.db')

    # Setter inn ekseempeldata
    c = db.cursor()
    value = random.randint(0, 30)
    date = time.time()

    for _ in range(10):
        value = random.randint(0, 30)
        date = time.time()

        sql_insert = f'INSERT INTO sensordata (value, date) VALUES ({value}, {date})'
        print(sql_insert)
        c.execute(sql_insert)
        
    db.commit()