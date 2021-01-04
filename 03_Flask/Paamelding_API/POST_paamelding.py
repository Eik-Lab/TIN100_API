import flask
from flask import request

import random

app = flask.Flask(__name__) #

paameldte = [] # "Databasen" vår som lagrer påmeldte


@app.route('/paamelding', methods=['POST'])
def paamelding():
    navn = request.args["navn"]
    paameldte.append(navn)
    print(paameldte)
    return f'{navn} er nå påmeldt'


app.run(debug=True)


# http://127.0.0.1:5000/paamelding?navn=Jørgen