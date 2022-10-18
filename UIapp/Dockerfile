FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

Copy ./requirements.txt

RUN pip install -r requirements.txt

COPY ./app