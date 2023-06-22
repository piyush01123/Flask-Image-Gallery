FROM python:3.8.2-slim-buster
RUN pip install flask
COPY . /app/
WORKDIR /app/
