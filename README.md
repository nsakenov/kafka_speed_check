# Kafka Speed Check 

[![Kafka](https://img.shields.io/badge/streaming_platform-kafka-black.svg?style=flat-square)](https://kafka.apache.org)
[![Docker Images](https://img.shields.io/badge/docker_images-confluent-orange.svg?style=flat-square)](https://github.com/confluentinc/cp-docker-images)
[![Python](https://img.shields.io/badge/python-3.5+-blue.svg?style=flat-square)](https://www.python.org)

This is the supporting repository for a project: [Tesla speed check with Kafka and Flutter Web](https://nurbolsakenov.com/tech/tesla-speed-check).

![Design](https://raw.githubusercontent.com/nsakenov/kafka_speed_check/master/architecture.png)

## Install

The backend part of the project is fully containerised. You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.


## Quickstart

- In the project directory (where the docker-compose.yml located), spin up the local single-node Kafka cluster:

```bash
$ docker compose up
```

- Check the cluster is up and running (wait for "started" to show up):

```bash
$ docker-compose logs -f broker | grep "started"
```


## Usage

Show a stream of transactions in the **speed.check** topic (optionally add `--from-beginning`):

```bash
$ docker-compose exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic speed.check
```

Topics:

- `current.speed`: current speed provided by the user of Flutter Web application
- `speed.check`: processed speed from the upstream consumer

Example current.speed:

```json
111
```
Example speed.check result:
```
{'speed': 111, 'exceeds': True}
```

## Teardown

To stop the transaction generator and fraud detector:

```bash
$ docker compose down
```

To stop the Kafka cluster (use `down`  instead to also remove contents of the topics):

```bash
$ docker compose stop
```

To remove the Docker containers:

```bash
$ docker compose rm
```
