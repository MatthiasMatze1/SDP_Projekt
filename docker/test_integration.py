# import pytest
# from flask import Flask
# from flask import Blueprint
# import psutil

# app = Flask(__name__)
# bp = Blueprint('cpu', __name__, url_prefix='/cpu')
# bptemp = Blueprint('temp', __name__, url_prefix='/cpu/temp')
# bpdisk = Blueprint('disk', __name__, url_prefix='/disk')

# app.register_blueprint(bp)
# app.register_blueprint(bptemp)
# app.register_blueprint(bpdisk)

# #@pytest.mark.integration
# #def test_cpu_auslastung_integration():
# #    with app.test_client() as client:
# #        response = client.get('/cpu/auslastung')
# #        assert response.status_code == 200
# #        assert b'CPU Auslastung ist' in response.data

# @pytest.mark.integration
# def test_cpu_temperatur_integration():
#     with app.test_client() as client:
#         response = client.get('/cpu/temp')
#         assert response.status_code == 200
#         assert b'Sys Temperatur ist' in response.data

# @pytest.mark.integration
# def test_cpu_temperatur_error_integration():
#     with app.test_client() as client:
#         response = client.get('/cpu/temp/error')
#         assert response.status_code == 200
#         assert (b'Temperatur zu hoch |' in response.data) or (b'Temperatur in Ordnung |' in response.data)

# @pytest.mark.integration
# def test_ram_integration():
#     with app.test_client() as client:
#         response = client.get('/cpu/ram')
#         assert response.status_code == 200
#         assert b'Freier Sys RAM' in response.data

# @pytest.mark.integration
# def test_disk_usage_integration():
#     with app.test_client() as client:
#         response = client.get('/disk/usage')
#         assert response.status_code == 200
#         assert b'Disk Usage ist' in response.data
