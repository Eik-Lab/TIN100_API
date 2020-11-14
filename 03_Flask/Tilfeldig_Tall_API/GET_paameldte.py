import flask
from flask import request, jsonify

import random

app = flask.Flask(__name__) #

paameldte = ["Jørgen", "Kristian", "Uzair"] # "Databasen" vår som lagrer påmeldte


@app.route('/paamelding', methods=['GET'])
def paamelding():
    return jsonify(paameldte)
    

app.run(debug=True)


# http://127.0.0.1:5000/paamelding