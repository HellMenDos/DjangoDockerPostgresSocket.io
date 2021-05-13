FROM python:3.6

RUN mkdir /app


COPY ./api/requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

COPY ./api/ /app

