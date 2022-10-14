from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    greetings = "Hello HBNB! This will be myfirst flask appliation"
    return greetings
