import flask
from flask import request, jsonify

import random

app = flask.Flask(__name__) #

paameldte = [] # "Databasen" vår som lagrer påmeldte


@app.route('/paamelding', methods=['GET', 'POST']) # Dette endepunktet kan ta imot både GET og POST-requester
def paamelding():
    if request.method == 'POST':
        navn = request.args["navn"]
        paameldte.append(navn)
        print(paameldte)
        return f'{navn} er nå påmeldt'
    elif request.method == 'GET':
        return jsonify(paameldte)

app.run(debug=True) # Starter applikasjonen på port 5000


# http://127.0.0.1:5000/paamelding
# http://127.0.0.1:5000/paamelding?navn=Jørgen