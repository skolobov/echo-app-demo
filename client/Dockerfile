FROM python:3.9-alpine

ARG PORT=5000

RUN mkdir -p /app/templates
WORKDIR /app

COPY app.py requirements.txt templates /app/

RUN pip3 install -r requirements.txt

EXPOSE ${PORT}
ENV FLASK_APP="app"

CMD flask run -h 0.0.0.0 -p ${PORT:-5000}
