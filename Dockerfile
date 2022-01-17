FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

COPY ./dependencies /app/dependencies

RUN pip install -r dependencies