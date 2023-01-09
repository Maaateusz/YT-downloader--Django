FROM python:alpine3.17
# FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# ffmpeg potrzebny do pydub
RUN apk add --no-cache ffmpeg

COPY . /code/