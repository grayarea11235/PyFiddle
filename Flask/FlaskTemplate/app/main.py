import logging
import flask
import psutil

from flask import Flask
from flask import render_template

from app_system_info import AppSystemInfo


app = Flask(__name__)

logging.basicConfig(filename='logfile.log', level=logging.INFO)


@app.route('/info')
def flask_info():
    system_info = AppSystemInfo(app)

    return render_template('info.html', system_info=system_info)


@app.route('/base')
def do_base():
    return render_template('base.html')


@app.route('/defaultapp')
def default_app():
    return 'Default App'


@app.route('/top')
def top_page():
    return render_template('top.html')


@app.route('/sysinfo', methods=['GET'])
def sys_info():
    ps_info = dict()

    #for proc in psutil.process_iter():
        #print(proc.pid); 

    return str(psutil.os.cpu_count())


@app.route('/')
def hello_world():
   return '<b>Holding page</b>' 
