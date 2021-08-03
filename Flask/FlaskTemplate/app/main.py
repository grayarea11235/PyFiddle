import logging
import flask

from flask import Flask
from flask import render_template

from app_system_info import AppSystemInfo


app = Flask(__name__)

logging.basicConfig(filename='logfile.log', level=logging.INFO)


@app.route('/info')
def flask_info():
    logging.info('In flask_info')
    system_info = AppSystemInfo(app)

    return render_template('info.html', system_info=system_info)


@app.route('/base')
def do_base():
    return render_template('base.html')


@app.route('/')
def hello_world():
    return 'Hello, World!'
