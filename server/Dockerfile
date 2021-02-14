FROM golang:1.15-alpine

RUN mkdir /app
COPY main.go go.mod go.sum /app/
WORKDIR /app

RUN go build -o server .

CMD [ "/app/server" ]
