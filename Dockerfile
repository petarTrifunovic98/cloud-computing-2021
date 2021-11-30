FROM ubuntu:20.04

RUN apt-get update && apt-get -y install pip && pip install django
WORKDIR /usr/src