Start with:

I have created a python venv for managing python libs


Python libs installed:
Flask (obviously :D )
psutils (for CPU parameters)

TODO: Reuirements file for libs

Python venv can be started with:  source venv/bin/activate
Export flask app to start it with: export FLASK_APP=hello
Execute flask program: flask run --host=0.0.0.0

for help see 

https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/



------------
-Standard Blueprint used

-All possible URLs:
raspberrypi:80/cpu/temp
http://raspberrypi.local:5000/cpu/auslastung
http://raspberrypi.local:5000/cpu/temp


------------------
build docker image:

go into main directory and run
> docker build docker 

param:
-docker: directory containing docker file

----
build docker image :
>sudo docker build docker


----
start all of this with 
the last param is the id of the docker image created during build
pi@raspberrypi:~/Desktop/SDP $ docker run -p 80:5000 a9ffe2cb865c

access via webbrowser (or ip address)
>http://raspberrypi.local/cpu/auslastung


----------
after running the docker image you are ready to go for the test

This test_file(test_app.py) contains a sample test file for monitoring CPU usage, CPU temperature, and disk usage using Python and the psutil library. The test file uses the Flask framework for creating a web server that exposes the monitoring information through different endpoints. The test file also uses the pytest framework for unit and integration testing.
Prerequisites

To run the tests, you will need to have the following software installed on your machine:

    Python 3
    Pytest
if you do not have pytest.install it with this command on the terminal.
pip install pytest. 
you can check the version of your pytest with this command.
pytest --version
You also need to have access to the code that the test file is testing, and it should be running on the same machine or accessible through the network.
Running the tests.

To run the tests, navigate to the directory where the test file is located and run the following command:

pytest test_app.py
if you would like to have more detail about the testrun this command.
pytest test_app.py -v


This command runs all the tests defined in the test file. The tests check the correctness of the monitoring information returned by the different endpoints and the behavior of the code under different conditions.
Test Categories

The tests are divided into 4 main categories:

    test_cpu_auslastung, test_cpu_temp, test_cpu_temp_error, test_disk_usage: These tests check the correctness of the data returned by the different endpoints. The endpoints are /cpu/auslastung, /cpu/temp/, /cpu/temp/error, /disk/usage respectively. The tests assert that the response status code is 200 and that the response data matches the expected output.
    test_integration: This test checks if all endpoints are working correctly together. The test asserts that the response status code is 200 and that the response data matches the expected output for each endpoint.
    test_auslastung, test_lowcpu, test_disk: These tests check the behavior of the code when certain conditions are met. The tests use the mocker fixture to patch the psutil.cpu_percent and psutil.disk_usage functions and simulate different conditions. The tests assert that the response status code is 200 and that the response data matches the expected output for each endpoint.

You can check the coverage of your tests by using a tool such as coverage.py
First, you will need to install the coverage package by running:

pip install coverage

hen, you can run your tests with coverage measurement by using the coverage run command, followed by the command to run your tests. For example:

coverage run -m pytest
Once the tests have completed, you can generate a coverage report using the coverage report command. This will show you the percentage of lines in your code that have been executed by the tests.

You can also generate a detailed report in HTML format using coverage html command. This will create a folder named 'htmlcov' in the same directory where you ran the command and you can open the index.html in your browser.

Here is an example of how to check the coverage:

coverage run -m pytest
coverage report
coverage html
if you're using a package like pytest-cov you can use the pytest --cov=<module_name> command to check the coverage in the same command of running the tests.

You can also specify the minimum coverage percentage that you want to achieve by using the `--cov-fail-under=<

Conclusion

This test file provides a comprehensive way of testing the monitoring application that exposed through different endpoints. It covers different scenarios and conditions that the application might encounter. However, it's important to note that this test file is just a sample and it might need to be modified or expanded based on the actual implementation of the application.
