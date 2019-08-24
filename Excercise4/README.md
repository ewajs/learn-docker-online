# Excercise 4

## Description
In this excercise, a database, a web server connecting to it, and an nginx load balancer forwarding requests between the Docker host and the webserver will be spin up in three different containers, interconnected by a User Defined Network.
This will include the creation of an nginx load balancer image `ewajs/lb:latest` made possible by the Dockerfile and associated files in this folder.

This sequence of commands with the files provided in this folder will:

- Create a User Defined Network.
- Build an ngnix load balancer image from the Dockerfile.
- Start up a postgres database, configured with the data provided via app.env.
- Start a Demo web server from the image jfahrer/demo_web_app:latest.
- Start the ngnix load balancer image, forwarding it's port 80 to the host's port 80.

## Set Up
Make sure the start.sh will be executable before copying it into the image by:
```
chmod +x start.sh
```

## Docker commands

```
docker network create mynet

docker image build -t ewajs/lb:latest .

docker container run -d --network mynet --name db --env-file app.env postgres

docker container run -d --network mynet --name webapp --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --name lb --env-file app.env -p 80:80 ewajs/lb:latest
```

## Cleanup
To stop and delete all resources:

```
docker container stop $(docker container ls -q)

docker container rm $(docker container ls -aq)

docker network rm mynet
```
