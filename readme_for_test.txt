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
check the output of the test by running the pytest command in the terminal.

use a command like docker exec to run the tests inside the container
You can also add the -v flag to the pytest command to see more detailed output, such as the names of the test functions being run and their output.

To check the coverage of the test, you can use the coverage library by running the command coverage run -m pytest. This will run the test and generate a coverage report.

Then you can see the coverage report by running coverage report -m to see the coverage of each file.

You can also generate a html report for better visualization, by running coverage html then open the htmlcov/index.html file to see the coverage report.