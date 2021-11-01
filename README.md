# CRM-service

CRM API based on [Django](https://www.djangoproject.com) and
[Docker](https://www.docker.com). It uses
[PostgreSQL](https://www.postgresql.org) for persistent storage, and
[Kubernetes](https://kubernetes.io) for deployments.

## Architecture

TBD

## Local testing

We can spin up both API and db with `docker-compose`. Use this sequence of
commands to bootstrap a local environment:

1. docker-compose up --build -d
1. docker-compose exec web python manage.py migrate
1. docker-compose exec web python manage.py createsuperuser

You should have now django listening on http://localhost:8000/

## Swagger

We've added support for OpenAPI specs on `/swagger` path.

## Tests

### Unit tests

TBD

### Integration tests

TBD

### Linters

 * [Black](https://black.readthedocs.io/) for python linter
 * [Hadolint](https://github.com/hadolint/hadolint) for Dockerfile

## Contributions

TBD

## Author

Juan Carlos Castillo Cano <jccastillocano@gmail.com>
