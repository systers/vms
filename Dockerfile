# Base Image
FROM python:3.6
MAINTAINER Tapasweni Pathak <tapaswenipathak@gmail.com>
EXPOSE 8000

# Initializing working dir
WORKDIR /usr/src
RUN mkdir vms
RUN cd vms

# Re-Initialize the working dir
WORKDIR /usr/src/vms

# Making the Copy of the requirements
COPY requirements.txt /usr/src/vms/requirements.txt

# Installing the requirements
RUN apt-get install libpq-dev

RUN pip install -r requirements.txt

# Updated By
LABEL HUSSAIN="husainattar110@gmail.com"
