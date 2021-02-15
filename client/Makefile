IMAGE=skolobov/echo-client
VERSION=0.1.4

all: build push

build:
	docker build -t ${IMAGE}:${VERSION} .

push:
	docker push ${IMAGE}:${VERSION}

clean:
	rm server
