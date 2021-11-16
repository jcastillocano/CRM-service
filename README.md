# CRM-service

CRM API based on [Django](https://www.djangoproject.com) and
[Docker](https://www.docker.com). It uses
[PostgreSQL](https://www.postgresql.org) for persistent storage, and
[Kubernetes](https://kubernetes.io) for deployments.

## Architecture

This API provides two different endpoints: *customer* and *user*. There is
also a backoffice endpoint for admins to manage resources directly on web.

For managing *customer* information authentication is required (user:pass
base64 encoded in `Authorization: Bearer` header. For managing *user*
information admin privileges are also required.

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
 
### Backoffice
 
Django Admin site for managing Customer and Users from a web dashboard
 
![Screenshot 2021-11-03 at 17 30 18](https://user-images.githubusercontent.com/185361/140158903-b12f038b-253e-4d48-a7ff-b16065777a3d.png)

To access this admin backoffice use internal port 8080.

## Local testing

We can spin up both API and db with `docker-compose`. Use this sequence of
commands to bootstrap a local environment:

1. docker-compose up --build -d
1. docker-compose exec web python manage.py migrate
1. docker-compose exec web python manage.py createsuperuser

You should have now django listening on http://localhost:8888/. Metrics and
admin site are available on http://localhost:8080/.

## Swagger

We've added support for OpenAPI specs on `/swagger` path. Feel free to try out
this API using different rest methods available.

![Screenshot 2021-11-03 at 17 27 31](https://user-images.githubusercontent.com/185361/140155573-c6529e47-a991-42d2-b4b0-f2e1028b3fd9.png)

## Tests

### Unit tests

Use this command for running unit tests we need to run:

`python manage.py test`

### Linters

 * [Black](https://black.readthedocs.io/) for python linter
 * [Hadolint](https://github.com/hadolint/hadolint) for Dockerfile
 
## Deployments
 
This repository provides a Helm chart (_k8s_ folder) to automate deployments on
a kubernetes cluster (with LoadBalancer support). For that, please follow these
steps:

1. Create namespace `kubectl create namespace crm`

### Initialize postgres db

NOTE: for testing purposes, for production environments use a dedidated
postgres instance (i.e. RDS)

1. `helm repo add bitnami https://charts.bitnami.com/bitnami`
1. `helm install postgres bitnami/postgresql -n crm --set postgresqlPassword=secretpassword,postgresqlDatabase=crm`


### Deploy chart

NOTE: provide your chart config values (check _k8s/values.yaml_ for defaults)
as a yaml file. Then, run this command to install/update this repository:

1. `helm upgrade --atomic --install crm ./k8s -f test.yaml -n crm`

After that you should have your env almost ready. Last bits would be to apply
migrations and create superuser as follows:

1. `kubectl get po -n crm | grep crm-service` (take note of pod name)
1. `kubectl exec -ti <pod_name> -n crm -- python manage.py migrate`
1. `kubectl exec -ti <pod_name> -n crm -- python manage.py createsuperuser`

After that, your service should be listening on an ALB, we can get its domain
with `kubectl get svc -n crm`. For backoffice, it is recommended to use
*port-forward* with `kubectl port-forward -n crm svc/crm-crm-service 8080:8080`.
That will listen on localhost:8000 for /metrics, /admin and /stub

## Monitoring
 
Added prometheus metrics on <domain>:8080/metrics url. 

Checkout https://grafana.com/grafana/dashboards/9528 for using these metrics in
grafana.

## Contributions

In order to contribute to this repository, please fork it and upload your
changes. Then you can create a pull request against main branch from your
forked repository.

## Author

Juan Carlos Castillo Cano <jccastillocano@gmail.com>
