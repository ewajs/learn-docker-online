# Excercise 6

In this excercise, a postgres database and a web server are spun up, both are configured by enviornment variable files called `db.env` and `app.env` respectively.
The containers are spun up, configured and interconnected via **Docker Compose**.
Docker compose will:

- Create a Docker Volume
- Create a User Defined Network
- Create a database container based off the image `postgres:9.6-alpine`, mounting the volume to it.
- Create a webserver container based off the image `jfahrer/demo_web_app:latest`.
- Expose port 9292 of the container to port 80 of the host.

# Start the containers

To start, move the working directory to the folder `Excercise6` and issue the following command:

```
docker-compose up
```

# Stop the containers

To stop all container and delete all resources, _except for the volumes_ issue the following command:

```
docker-compose down
```
