FROM python:3.9-alpine

ARG HOST="0.0.0.0"
ARG PORT="5000"

RUN mkdir /app
WORKDIR /app

COPY app.py requirements.txt templates /app/

RUN pip3 install -r requirements.txt

EXPOSE ${PORT}
ENV FLASK_APP="app"

CMD ["flask", "run", "--host", "${HOST}", "--port", "${PORT}" ]
