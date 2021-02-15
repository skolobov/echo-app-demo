IMAGE=skolobov/echo-client
VERSION=0.1.5

all: build push

build:
	docker build -t ${IMAGE}:${VERSION} .

push:
	docker push ${IMAGE}:${VERSION}

clean:
	rm -rf __pycache__
