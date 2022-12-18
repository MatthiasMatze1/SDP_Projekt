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
http://raspberrypi.local:5000/cpu/ram
http://raspberrypi.local:5000/cpu/auslastung
http://raspberrypi.local:5000/cpu/temp
