FROM python:3.9.0-buster
MAINTAINER kiarash3012

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a nonroot user, and switch to it
RUN /usr/sbin/useradd --create-home --home-dir /usr/local/djangoadmin --shell /bin/bash djangoadmin
RUN /usr/sbin/adduser djangoadmin sudo
RUN chown -R djangoadmin /usr/local/
RUN chown -R djangoadmin /usr/lib/
RUN chown -R djangoadmin /usr/bin/
RUN chown -R djangoadmin /app

RUN /bin/su djangoadmin
