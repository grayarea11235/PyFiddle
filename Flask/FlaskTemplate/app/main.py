import sys

import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/info')
def flask_info():
    print('In flask_info')
    ex = sys.executable  # Python executable
    flask_version = flask.__version__

    return render_template('info.html', executable=ex, flask_version=flask_version)


@app.route('/')
def hello_world():
    return 'Hello, World!'
