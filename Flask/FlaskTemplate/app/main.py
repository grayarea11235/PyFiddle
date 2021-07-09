import sys
import platform
from app_system_info import AppSystemInfo

import logging


import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

logging.basicConfig(filename='logfile.log', level=logging.INFO)

@app.route('/info')
def flask_info():
    logging.info('In flask_info')
    system_info = AppSystemInfo(app)

    return render_template('info.html', system_info=system_info)


@app.route('/')
def hello_world():
    return 'Hello, World!'
