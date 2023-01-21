import pytest
from flask import Flask
from flask import Blueprint
import psutil
from app import app, bp, bptemp, bpdisk
from flask.testing import FlaskClient

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
@pytest.mark.unit
def test_cpu_auslastung(client):
    response = client.get('/cpu/auslastung')
    assert response.status_code == 200
    assert response.data.decode() == "CPU Auslastung ist 0.0%"

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


