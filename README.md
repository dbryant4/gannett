# Hello World App

This is a basic Hello World web application.

# Requirements

- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (Docker for Mac or Docker-CE/EE)
- [dgoss](https://github.com/aelsabbahy/goss/tree/master/extras/dgoss) - for container tests

# Getting Started

1. Run application acceptance tests.

  ```
  docker run -v ${PWD}:/app -e PYTHONPATH=/app python:2.7  bash -c "pip install -r /app/requirements.txt -r /app/tests/requirements.txt && pytest /app/tests"
  ```

2. Deactivate and delete virtualenv

  ```
  deactivate
  rm -rf venv
  ```

3. Next, build a container image.

  ```
  docker build -t hello_world_app:latest .
  ```

4. Then, test the container image using dgoss:

  ```
  dgoss run hello_world_app:latest
  ```

5. Start the application:

  ```
  docker run --rm -d -p 8080:8080 --name my_app hello_world_app:latest
  ```

6. Point your web browser to <http://127.0.0.1:8080/>. "hello world" should be returned.

7. To stop the container:

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

# Tests

To run tests,
