# syntax=docker/dockerfile:1
FROM python:3.9-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install Django==4.1.2 --user
RUN pip3 install -r requirements.txt --user
COPY . /code/