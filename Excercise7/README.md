# Excercise 7

In this excercise, a postgres database, a web server, and a load balancer are spun up, both are configured by enviornment variables listed in the file called `.env`. The `lb` and `webapp` containers will be created with **dependencies** on `pg` and `webapp` containers respectively. This means, that `docker-compose up` will create the containers in the correct order, however, this does not ensure that, for example, `pg` is **ready** for `webapp` to depend on, that needs to be handled by the container logic itself, docker-compose will only ensure the order of creation.
The containers are spun up, configured and interconnected via **Docker Compose**.
Docker compose will:

- Create a Docker Volume
- Create a User Defined Network
- Create a database container based off the image `postgres:9.6-alpine`, mounting the volume to it.
- Create a webserver container based off the image `jfahrer/demo_web_app:wait_for_pg`, depending on the database container.
- Create a load balancer container based off the image `ewajs/lb:latest`, depending on the webserver container.
- Expose port 80 of the load balancer container to port 80 of the host.

# Start the containers

To start, move the working directory to the folder `Excercise7` and issue the following command:

```
docker-compose up
```

# Stop the containers

To stop all container and delete all resources, _except for the volumes_ issue the following command:

```
docker-compose down
```
