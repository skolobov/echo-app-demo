FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

COPY app.py requirements.txt templates /app/

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
