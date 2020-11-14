import flask
from flask import request

import random

app = flask.Flask(__name__) #


@app.route('/tilfeldig_tall', methods=["GET"])
def tilfeldig_tall():
    # Det er mulig å få tilgang til parameterene i requesten ved å bruke request.args
    start = int(request.args["start"])
    end = int(request.args["end"])
    return {"tilfeldig_tall": random.randrange(start, end)}


app.run(debug=True)


# http://127.0.0.1:5000/?start=3&end=10