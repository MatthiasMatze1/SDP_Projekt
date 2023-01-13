 # syntax=docker/dockerfile:1
 
 FROM arm32v6/python:3.9-alpine AS base
 # Angabe: includes everything that all targets need 
 # docker build -t docker --target prod -> multistage docker zeugs

# gcc needed for python RPi.GPIO library
RUN echo "--------------------BUILDING BASE IMAGE--------------------"
RUN apk update
RUN apk add python3-dev \
            gcc \
            libc-dev \
            libffi-dev

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#
RUN pip install --upgrade pip 

WORKDIR /SDP

ENV FLASK_APP=app
EXPOSE 5000
COPY requirements/base.txt base.txt

RUN pip3 install -r base.txt

COPY . .

CMD ["FLASK_APP=app"]
CMD ["python3","-m","flask","run","--host=0.0.0.0"]
#
#-----------------------------------------DEVELOPMENT------------------------------------------------------------------

FROM base AS development
#Angabe:will start Flask server in debug mode
#       flask --debug run --host=0.0.0.0
# gcc needed for python RPi.GPIO library
#RUN apk update
#RUN apk add python3-dev \
 #           gcc \
 #          libc-dev \
 #          libffi-dev
RUN echo "--------------------BUILDING DEVELOPMENT IMAGE--------------------"

WORKDIR /SDP

ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 5000

#COPY --from=build requirements/dev.txt /tmp/
#COPY requirements/dev.txt /tmp/
COPY requirements/dev.txt dev.txt

#RUN pip3 install -r /tmp/dev.txt
#RUN pip3 install -r dev.txt

COPY . .

CMD ["FLASK_APP=app"]
CMD ["python3","-m","flask","run","--host=0.0.0.0"]
#-----------------------------------------TEST------------------------------------------------------------------

#Angabe:
#       -run linter (https://flake8.pycqa.org/en/latest/)
#       -run tests (first unit tests, then integration tests)
#           -coverage run -m pytest [...]
#       -check coverage
#           -coverage report [...]
#       -fails if test coverage is below 80%

#FROM base AS test

#RUN echo "--------------------BUILDING TEST IMAGE--------------------"


#COPY --from=base /opt/venv /opt/venv

#WORKDIR /SDP

#COPY --from=build requirements/test.txt test.txt

#RUN pip3 install -r test.txt

# Code mitkopieren -> geht schneller

#COPY app/ app/

#ENV PATH="/opt/venv/bin:$PATH"

# RUN ["flake8","app/"]


#-----------------------------------------PRODUCTION------------------------------------------------------------------
#FROM base AS production
RUN echo "build Production image"

RUN echo "--------------------BUILDING PRODUCTION IMAGE--------------------"


#WORKDIR /SDP

#ENV FLASK_APP=app
#ENV FLASK_ENV=development
#EXPOSE 5000

#COPY --from=build requirements/dev.txt /tmp/
#COPY requirements/prod.txt prod.txt


#RUN pip3 install -r /tmp/prod.txt

#COPY . .

#CMD ["FLASK_APP=app"]
#CMD ["python3","-m","flask","run","--host=0.0.0.0"]