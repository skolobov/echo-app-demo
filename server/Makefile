IMAGE=skolobov/echo-server
VERSION=0.1.1

all: build push

build:
	docker build -t ${IMAGE}:${VERSION} .

push:
	echo "${DOCKER_HUB_PASSWORD}" | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin
	docker push ${IMAGE}:${VERSION}

clean:
	rm server
