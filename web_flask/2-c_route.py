from glob import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    greeting = 'HELLO HBNB!'
    return greeting

@app.route('/hbnb')
def hello():
    greeting = 'HBNB!'
    return greeting

@app.route('/c/<text>')
def fun(text):
    return 'C %s' % escape(text)
