import flask
from flask import request, jsonify

import random

app = flask.Flask(__name__) #

paameldte = [] # "Databasen" vår som lagrer påmeldte


@app.route('/paamelding', methods=['GET', 'POST'])
def paamelding():
    if request.method == 'POST':
        navn = request.args["navn"]
        paameldte.append(navn)
        print(paameldte)
        return f'{navn} er nå påmeldt'
    elif request.method == 'GET':
        return jsonify(paameldte)

app.run(debug=True)


# http://127.0.0.1:5000/paamelding
# http://127.0.0.1:5000/paamelding?navn=Jørgen