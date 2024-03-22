# pull official base image
FROM python:3.10-alpine

# create directory for the app user
RUN mkdir -p /home

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 0

# create the appropriate directories
ENV HOME=/home
ENV APP_HOME=/home/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .
