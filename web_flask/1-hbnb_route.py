from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'Hello HBNB!'
    return greeting

@app.route('/hbnb')
def hello():
    greeting = "HBNB!"
    return greeting

