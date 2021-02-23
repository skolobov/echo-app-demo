# echo-app-demo

Demo App with Echo Server and Client

* Server is implemented in Go using:
  * [Go 1.15.7](https://golang.org/dl/)
  * [Echo 4.2.0](https://echo.labstack.com)
* Client is implemented in Python using:
  * [Python 3.9.1](https://www.python.org/downloads/)
  * [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
  * [WTForms 2.3.3](https://wtforms.readthedocs.io/en/2.3.x/)

## Installation in minikube

Start minikube cluster if it's not running:

```
minikube start
```

Install Echo App with Helm:

```
helm -n echo install --create-namespace  echo ./chart
```

## Usage

Open frontend service in a web browser:

```
minikube service -n echo echo-client
```
