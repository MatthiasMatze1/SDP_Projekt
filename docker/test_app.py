from flask import Flask, Blueprint
import psutil
#from docker import app
import pytest
from flask import Flask
import psutil
from app import app, bp, bptemp, bpdisk
from flask.testing import FlaskClient
import re


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
@pytest.mark.unit
def test_cpu_auslastung(client):
    response = client.get('/cpu/auslastung')
    assert response.status_code == 200
    # assert response.data.decode() == "CPU Auslastung ist 0.0%" 
    response = client.get('/cpu/auslastung')
    assert re.match("CPU Auslastung ist \d+\.\d+%",response.data.decode())


@pytest.mark.unit
def test_cpu_temp(client):
    response = client.get('/cpu/temp/')
    assert response.status_code == 200
    assert response.data.decode().startswith("Sys Temperatur ist")

@pytest.mark.unit
def test_cpu_temp_error(client):
    response = client.get('/cpu/temp/error')
    assert response.status_code == 200
    assert response.data.decode().startswith("Temperatur in Ordnung |")
@pytest.mark.integration
def test_integration(client):
    response = client.get('/cpu/auslastung')
    assert response.status_code == 200
    assert response.data.decode() == "CPU Auslastung ist 0.0%"
    response = client.get('/cpu/temp/')
    assert response.status_code == 200
    assert response.data.decode().startswith("Sys Temperatur ist")
    response = client.get('/cpu/temp/error')
    assert response.status_code == 200
    assert response.data.decode().startswith("Temperatur in Ordnung |")
    response = client.get('/disk/usage')
    assert response.status_code == 200
    assert response.data.decode().startswith("Disk Usage ist")


def test_auslastung(mocker):
    # Use the mocker fixture to patch the psutil.cpu_percent function
    mocker.patch("psutil.cpu_percent", return_value=50)

    # Use the client fixture to make a GET request to the '/cpu/auslastung' endpoint
    response = app.test_client().get('/cpu/auslastung')

    # Assert that the response has a 200 status code and the expected response data
    assert response.status_code == 200
    assert response.data.decode() == "CPU Auslastung ist 50%"

