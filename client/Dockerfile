FROM python:3.9-alpine

ARG FLASK_PORT

RUN mkdir /app
WORKDIR /app

COPY app.py requirements.txt templates /app/

RUN pip3 install -r requirements.txt

EXPOSE ${PORT}
ENV FLASK_APP="app"
ENV FLASK_PORT=${FLASK_PORT:-5000}

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "$FLASK_PORT" ]
