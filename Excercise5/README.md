# Excercise 5

## Description

This excercise builds on what was done on [**Excercise 4**](https://github.com/ewajs/learn-docker-online/tree/master/Excercise4), please check that out first.
A database, multiple web servers connecting to it, and an nginx load balancer forwarding requests between the Docker host and the webservers will be spun up in three different containers, interconnected by a User Defined Network.
This will make use of the nginx load balancer image `ewajs/lb:latest` built in the previous excercise (same Dockerfile and startup script from Excercise 4 are provided to make this self contained).

## Changes from Excercise 4

Some of the changes made to the original is the separation of the Environment Variable file into three different files, one for each kind of container.
The database container is also created with a Docker Volume to persist data beyond the postgres container's lifecycle.
This time, multiple web servers with network aliases are spun up, to prove the load balancing function.

This sequence of commands with the files provided in this folder will:

- Create a User Defined Network.
- Start up a postgres database, configured with the data provided via app.env and a Docker Volume mount.
- Start 5 Demo web servers from the image jfahrer/demo_web_app:latest with the same network alias.
- Start the ngnix load balancer image, forwarding it's port 80 to the host's port 80.

## Set Up

Make sure the start.sh will be executable before copying it into the image by:

```
chmod +x start.sh
```

## Docker commands

```
docker network create mynet

docker container run -d --network mynet --name db --env-file db.env --volume db_data:/var/lib/postgresql/data postgres

docker container run -d --network mynet --network-alias webapp --name app1 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app2 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app3 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app4 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app5 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --name lb --env-file lb.env -p 80:80 ewajs/lb:latest
```

## Cleanup

To stop and delete all resources:

```
docker container stop $(docker container ls -q)

docker container rm $(docker container ls -aq)

docker network rm mynet
```
