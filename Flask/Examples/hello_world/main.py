# This is a hello world Flask template

from flask import Flask
app = Flask(__name__)

app.route('/info')
def flask_info():
    return '<b>INFO!!!!!! INFO!</b>'


@app.route('/')
def hello_world():
    return 'Hello, World!'
