# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /opt/hello_flask
ADD . /opt/hello_flask

ENV PYTHONPATH=/opt/hello_flask
ENV PYTHONBUFFERED=1

RUN pip3 install -r /opt/hello_flask/requirements.txt
ENTRYPOINT [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]