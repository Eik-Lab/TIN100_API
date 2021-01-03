
from database import open_database
import flask
from flask import request, jsonify
import sqlite3


import time

app = flask.Flask(__name__)


@app.route('/insert', methods=["POST"])
def insert():

    with sqlite3.connect('sensordata.db') as con:
        c = con.cursor()
        value = request.args["value"]
        date = time.time()

        print(date)
        
        sql_insert = f'INSERT INTO sensordata (value, date) VALUES ({value}, {date})'
        print(sql_insert)
        c.execute(sql_insert)

        con.commit()

    return "suksess"

app.run(debug=True)