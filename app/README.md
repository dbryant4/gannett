# Gannett Hello World App

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Gannett Hello World App](#gannett-hello-world-app)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
	- [`/`](#)
	- [`/hello`](#hello)
	- [`/world`](#world)

<!-- /TOC -->

 This is a basic Hello World web application for Gannett.

# Requirements

- [Docker](https://www.docker.com/) (Docker for Mac or Docker-CE/EE)
- [dgoss](https://github.com/aelsabbahy/goss/tree/master/extras/dgoss) - for container tests

# Getting Started

1. Run application acceptance tests.

  ```
  docker run -v ${PWD}:/app -e PYTHONPATH=/app python:2.7  bash -c "pip install -r /app/requirements.txt -r /app/tests/requirements.txt && pytest /app/tests"
  ```

2. Next, build a container image.

  ```
  docker build -t gannett_hello_world_app:latest .
  ```

3. Then, test the container image using dgoss:

  ```
  dgoss run gannett_hello_world_app:latest
  ```

4. Start the application:

  ```
  docker run --rm -d -p 8080:8080 --name my_app gannett_hello_world_app:latest
  ```

5. Point your web browser to <http://127.0.0.1:8080/>. "hello world" should be returned.

6. To stop the container:

  ```
  docker kill my_app
  ```

# Endpoints

The endpoints below support the query parameters below. They can be used

- `uppercase` - Capitalizes the return string.
- `reversed` -

## `/`

- Method: GET

  Return Content: hello world

  Success Status Code: 200

## `/hello`

- Method: GET

  Return Content: hello

  Success Status Code: 200

## `/world`

- Method: GET

  Return Content: world

  Success Status Code: 200
