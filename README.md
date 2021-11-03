# CRM-service

CRM API based on [Django](https://www.djangoproject.com) and
[Docker](https://www.docker.com). It uses
[PostgreSQL](https://www.postgresql.org) for persistent storage, and
[Kubernetes](https://kubernetes.io) for deployments.

## Architecture

This API provides two different endpoints: *customer* and *user*.

For managing *customer* information authentication is required (user:pass
base64 encoded in `Authorization: Bearer` header. For managing *user*
infromation admin privileges are also required.

### Customer

Fields:

 * **first_name**: string
 * **last_name**: string
 * **photo**: binary

Endpoints:

 * GET /v1/customer --> list all customers
 * POST /v1/customer --> create new customer
 * GET /v1/customer/<id> --> get customer by id
 * PUT /v1/customer/<id> --> update customer by id
 * PATCH /v1/customer/<id> --> partial customer update by id
 * DEELETE /v1/customer/<id> --> delete customer by id

### User

Fields:

 * **first_name**: string
 * **last_name**: string
 * **username**: string
 * **password**: string
 * **email**: string
 * **is_superuser**: bool

Endpoints:

 * GET /v1/user --> list all users
 * POST /v1/user --> create new user
 * GET /v1/user/<id> --> get user by id
 * PUT /v1/user/<id> --> update user by id
 * PATCH /v1/user/<id> --> partial user update by id
 * DEELETE /v1/user/<id> --> delete user by id
 

## Local testing

We can spin up both API and db with `docker-compose`. Use this sequence of
commands to bootstrap a local environment:

1. docker-compose up --build -d
1. docker-compose exec web python manage.py migrate
1. docker-compose exec web python manage.py createsuperuser

You should have now django listening on http://localhost:8000/

## Swagger

We've added support for OpenAPI specs on `/swagger` path. Feel free to try out
this API using different rest methods available.

## Tests

### Unit tests

Use this command for running unit tests we need to run:

`python manage.py test`

### Linters

 * [Black](https://black.readthedocs.io/) for python linter
 * [Hadolint](https://github.com/hadolint/hadolint) for Dockerfile

## Contributions

In order to contribute to this repository, please fork it and upload your
changes. Then you can create a pull request against main branch from your
forked repository.

## Author

Juan Carlos Castillo Cano <jccastillocano@gmail.com>
