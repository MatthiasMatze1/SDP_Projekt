from flask import Flask
from flask import Blueprint
import psutil

app = Flask(__name__)

bp = Blueprint('cpu', __name__, url_prefix='/cpu')

@bp.route('/auslastung')
def auslastung():
    output = "CPU Auslastung ist " + str(psutil.cpu_percent(1)) + "%"
    return output

@bp.route('/temp')
def temperatur():
    output = "Sys Temperatur ist " + str(psutil.sensors_temperatures()) + "%"
    return output

@bp.route('/ram')
def ram():
    output = "Freier Sys RAM " + str(psutil.virtual_memory()[2]) + "%"
    return output

app.register_blueprint(bp)