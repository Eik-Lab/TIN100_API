import flask
from flask import request, jsonify

import random

app = flask.Flask(__name__) # Instansierer Flask-applikasjonen

paameldte = ["Jørgen", "Kristian", "Uzair"] # "Databasen" vår som lagrer påmeldte

# Endepunktet er /paamelding. Kan ta imot GET-requester
@app.route('/paamelding', methods=['GET'])
def paamelding():
    return jsonify(paameldte) # Konverterer listen til jsonify
    

app.run(debug=True) # Kjører serveren. Standardporten er port 5000
# app.run(port=1234) # Bruk port-argumentet for å endre porten programmet kjøres på

# http://127.0.0.1:5000/paamelding