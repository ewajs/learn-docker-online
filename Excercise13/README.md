# Excercise 12

This excercise builds up on what was done in [**Excercise 12**](https://github.com/ewajs/learn-docker-online/tree/master/Excercise12). Adding an ngnix Load Balancer and scaling up the webservers to 3 replicas.

Docker Compose will:

- Build/pull the image `ewajs/flask:latest` with web server code and dependencies.
- Create a Docker Volume
- Create a User Defined Network
- Create a database container based off the image `postgres:9.6-alpine`, mounting the volume to it. The container will initialize its database with a `requests` table.
- Create 3 webserver containers based off the image `ewajs/flask:latest`, depending on the database container. The `/app` directory in the host will be mounted to the `/app` directory in the container to override the image's source code.
- Create a load balancer nginx container, depending on the webserver containers, pointing it to the webserver container replicas.
- Expose port 80 of the load balancer container to port 80 of the host.

## Database Container

The Postgres database is initialized by the file `db/init.sql` by passing it as a bind mount to the Postgres container in its initialization sql script folder (see [Initialization Scripts in Postgres Image documentation](https://hub.docker.com/_/postgres)). This script will create a table to log server requests in. This container is also configured with a Docker Volume to persist database data between different containers. The database is configured by environment variables in the `.env` files as specified in the `docker-compose.yml` file.

## Webserver container

The webserver image can be built from the provided Dockerfile at `app/Dockerfile`. This image, based from `python:3.6-alpine` not only copies the source code of the application but also installs the necessary dependencies to connect to a postgres database. The web server is configured by environment variables in the `.env` files as specified in the `docker-compose.yml` file. Also, the `app` folder is mounted onto the container as a bind mount to allow for quick testing of the application code.
The webserver will log requests to the database and output dynamic HTML with the last 25 requests, including the one just made. Requests will persist in the database since the data is stored in a Docker Volume and mounted every time a new database container instance is created.

## Load Balancer container

The load balancer image can be built from the provided Dockerfile at `lb/Dockerfile`. This image, based from `ewajs/nginx:latest`. This image configures the nginx load balancer at startup to point the appropiate webserver(s) through the `PROXY_UPSTREAM` environment variable provided in the `.env` file. The load balancer will forward the requests from the host to the webservers with it's load balancing strategy.

## Starting the Services

To start everything (in daemon mode) run:

```
docker-compose up -d --scale webapp=3
```

You should be able to connect to the load balancer container by accessing port 80 of the container's host. You should see a Table containing all request data saved to the database by any of the webservers. These should persist unless you manually delete the volume created by Docker Compose, forcing it to create a new one next time you run `docker compose up`.

## Stopping the Services

Run:

```
docker-compose down
```

## Clean up

Docker Compose will handle all cleanup _except_ for the Database Docker Volume, to delete it, run:

```
docker volume rm VOLUME_NAME
```

Where `VOLUME_NAME` will be the mounted volume name, in this case `excercise12_pg_data`
