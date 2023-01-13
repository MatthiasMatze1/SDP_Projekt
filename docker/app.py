from flask import Flask
from flask import Blueprint
import psutil

app = Flask(__name__)

bp = Blueprint('cpu', __name__, url_prefix='/cpu')
bptemp = Blueprint('temp', __name__, url_prefix='/cpu/temp')
bpdisk = Blueprint('disk', __name__, url_prefix='/disk')


@bp.route('/auslastung')
def auslastung():
    output = "CPU Auslastung ist " + str(psutil.cpu_percent(1)) + "%"
    return output


@bptemp.route('/')
def temperatur():
    cpu_temp = psutil.sensors_temperatures()["cpu_thermal"][0]
    output = "Sys Temperatur ist " + str(cpu_temp.current) + chr(176) + "C"
    return output


@bptemp.route('/error')
def temperror():
    cpu_temp = psutil.sensors_temperatures()["cpu_thermal"][0]
    zu_hoch = "Temperatur zu hoch | "
    temp_ok = "Temperatur in Ordnung | "

    if cpu_temp.current >= 60:
        output = zu_hoch + str(cpu_temp.current) + chr(176) + "C"
    else:
        output = temp_ok + str(cpu_temp.current) + chr(176) + "C"
    return output


@bp.route('/ram')
def ram():
    output = "Freier Sys RAM " + str(psutil.virtual_memory()[2]) + "%"
    return output


@bpdisk.route('/usage')
def usage():
    output = "Disk Usage ist " + str(psutil.disk_usage('/').percent) + "%"
    return output


app.register_blueprint(bp)
app.register_blueprint(bptemp)
app.register_blueprint(bpdisk)
