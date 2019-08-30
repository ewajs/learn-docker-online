# Excercise 12

This excercise builds up on what was done in [**Excercise 11**](https://github.com/ewajs/learn-docker-online/tree/master/Excercise11). Adding a database container to log the requests to the web server.

Docker Compose will:

- Build/pull the image `ewajs/flask:latest` with web server code and dependencies.
- Create a Docker Volume
- Create a User Defined Network
- Create a database container based off the image `postgres:9.6-alpine`, mounting the volume to it. The container will initialize its database with a `requests` table.
- Create a webserver container based off the image `ewajs/flask:latest`, depending on the database container. The `/app` directory in the host will be mounted to the `/app` directory in the container to override the image's source code.
- Expose port 80 of the webserver container to port 80 of the host.

## Database Container

The Postgres database is initialized by the file `db/init.sql` by passing it as a bind mount to the Postgres container in its initialization sql script folder (see [Initialization Scripts in Postgres Image documentation](https://hub.docker.com/_/postgres)). This script will create a table to log server requests in. This container is also configured with a Docker Volume to persist database data between different containers. The database is configured by environment variables in the `.env` files as specified in the `docker-compose.yml` file.

## Webserver container

The webserver image can be built from the provided Dockerfile at `app/Dockerfile`. This image, based from `python:3.6-alpine` not only copies the source code of the application but also installs the necessary dependencies to connect to a postgres database. The web server is configured by environment variables in the `.env` files as specified in the `docker-compose.yml` file. Also, the `app` folder is mounted onto the container as a bind mount to allow for quick testing of the application code.
The webserver will log requests to the database and output a JSON containing the full request log, including the one just made. Requests will persist in the database since the data is stored in a Docker Volume and mounted every time a new database container instance is created.

## Starting the Services

To start everything (in daemon mode) run:

```
docker-compose up -d
```

You should be able to connect to the container by accessing port 80 of the container's host. You should see a JSON Array of Arrays containing all request data saved to the database. These should persist unless you manually delete the volume created by Docker Compose, forcing it to create a new one next time you run `docker compose up`.

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
