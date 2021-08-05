from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola Mundo"

@app.route("/json")
def users():
    users = [
        {'name': 'belloma'},
        {'name': 'tito'},
        {'name': 'riquelme'}
    ]
    response = app.response_class(response=json.dumps(users), status = 200, mimetype='application/json')
    return response

app.run(port=5000, debug=True)