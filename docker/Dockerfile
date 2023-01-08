 # syntax=docker/dockerfile:1
 
 FROM arm32v6/python:3.9-alpine AS base
 # Angabe: includes everything that all targets need 
 # docker build -t docker --target prod -> multistage docker zeugs

# gcc needed for python RPi.GPIO library
RUN apk update
RUN apk add python3-dev \
            gcc \
            libc-dev \
            libffi-dev

WORKDIR /SDP

ENV FLASK_APP=app
EXPOSE 5000
COPY requirements/base.txt base.txt

RUN pip3 install -r base.txt

COPY . .

CMD ["FLASK_APP=app"]
CMD ["python3","-m","flask","run","--host=0.0.0.0"]

#---------------------------------------------------------------------------------
#FROM arm32v6/python:3.9-alpine AS development
#Angabe:will start Flask server in debug mode
#       flask --debug run --host=0.0.0.0
# gcc needed for python RPi.GPIO library
#RUN apk update
#RUN apk add python3-dev \
#            gcc \
 #           libc-dev \
 #           libffi-dev

#WORKDIR /SDP

#ENV FLASK_APP=app
#ENV FLASK_ENV=development
#EXPOSE 5000

#COPY requirements/dev.txt /tmp/

#RUN pip3 install -r /tmp/dev.txt

#COPY . .

#CMD ["FLASK_APP=app"]
#CMD ["python3","-m","flask","run","--host=0.0.0.0"]
#---------------------------------------------------------------------------------
#FROM arm32v6/python:3.9-alpine AS test
#Angabe:run linter (https://flake8.pycqa.org/en/latest/)
#       run tests (first unit tests, then integration tests)
#       coverage run -m pytest [...]
#       check coverage
#       coverage report [...]
#       fails if test coverage is below 80%
#       FROM arm32v6/python:3.9-alpine AS production
