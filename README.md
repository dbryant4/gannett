# Gannett Take Home Challenge

## Overview

This is the take home challenge for the Gannett interview process.

See the [README.md](app/README.md) file in the `app/` directory for details of the application that is being packaged up and tested.

Below are the steps to create a local instance of [Concourse CI]

## Requirements

- [Docker](https://www.docker.com/) (Docker for Mac or Docker-CE/EE)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Hub Repository](https://hub.docker.com/)

## Getting Started

1. Start the Concourse CI instance

  ```
  docker-compose up -d
  ```

2. Open <http://127.0.0.1:8080/> in your browser, download `fly` for your OS, and place in your $PATH.

3. Login to the Concourse CI instance:

  `fly -t local login -c http://127.0.0.1:8080`

4. Create the `credentials.yml` file:

  ```
  ---
  DOCKER_REPO: dbryant4/gannett_hello_world_app
  DOCKER_USER: dbryant4
  DOCKER_MAIL: my_email_Address
  DOCKER_PASS: my_password
  ```

5. Create the concourse pipeline

  ```
  fly -t local set-pipeline -c concourse.yml -p helloworld -l credentials.yml
  ```

6. Un-pause the pipeline

  ```
  fly -t local unpause-pipeline -p helloworld
  ```

7. Trigger a build:

  ```
  fly -t local trigger-job  --job helloworld/hello-world
  ```

8. Visit the build in your browser

  <http://127.0.0.1:8080/teams/main/pipelines/helloworld/jobs/hello-world/builds/1>

9. Once you have finished building, destroy the Concourse CI instance so as to not waste space.

  ```
  docker-compose down
  ```
