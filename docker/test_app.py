import pytest
from app import app
import re
import psutil


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


@pytest.mark.unit
def test_cpu_auslastung(client):
    response = client.get('/cpu/auslastung')

    assert response.status_code == 200
    response = client.get('/cpu/auslastung')
    assert re.match(r"CPU Auslastung ist \d+\.\d+%", response.data.decode())


@pytest.mark.unit
def test_cpu_temp(client):
    response = client.get('/cpu/temp/')
    assert response.status_code == 200
    assert response.data.decode().startswith("Sys Temperatur ist")


@pytest.mark.unit
def test_cpu_temp_error(client):
    response = client.get('/cpu/temp/error')
    assert response.status_code == 200
    assert response.data.decode().startswith("Temperatur ")


@pytest.mark.unit
def test_disk_usage(client):
    response = client.get('/disk/usage')
    assert response.status_code == 200
    assert response.data.decode().startswith("Disk ")


@pytest.mark.integration
def test_integration(client):
    response = client.get('/cpu/auslastung')
    assert response.status_code == 200
    response = client.get('/cpu/auslastung')
    assert re.match(r"CPU Auslastung ist \d+\.\d+%", response.data.decode())
    response = client.get('/cpu/temp/')
    assert response.status_code == 200
    assert response.data.decode().startswith("Sys Temperatur ist")
    response = client.get('/cpu/temp/error')
    assert response.status_code == 200
    assert response.data.decode().startswith("Temperatur")
    response = client.get('/disk/usage')
    assert response.status_code == 200
    assert response.data.decode().startswith("Disk Usage ist")


def test_auslastung(mocker):
    # Use the mocker fixture to patch the psutil.cpu_percent function
    mocker.patch("psutil.cpu_percent", return_value=50)

    # Use the client fixture to make a GET request to the '/cpu/auslastung' endpoint
    response = app.test_client().get('/cpu/auslastung')

    # Assert that the response has a 200 status code and
    # the expected response data
    assert response.status_code == 200
    assert response.data.decode() == "CPU Auslastung ist 50%"


def test_lowcpu(mocker):
    mocker.patch("psutil.cpu_percent", return_value=10)
    response = app.test_client().get('/cpu/auslastung')
    assert response.status_code == 200
    assert response.data.decode() == "CPU Auslastung ist 10%"


def test_disk(mocker):
    # Use the mocker fixture to patch the psutil.disk_usage function
    mocker.patch("psutil.disk_usage", return_value=psutil._common.sdiskusage
            (total=1000, used=500, free=500, percent=50))

    # Use the client fixture to make a GET request to the '/disk/usage' endpoint
    response = app.test_client().get('/disk/usage')

    # Assert that the response has a 200 status code and the expected response data
    assert response.status_code == 200
    assert response.data.decode() == "Disk Usage ist 50%"
