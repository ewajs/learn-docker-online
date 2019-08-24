#!/usr/bin/env bash

docker network create mynet

docker container run -d --network mynet --name db --env-file db.env --volume db_data:/var/lib/postgresql/data postgres

docker container run -d --network mynet --network-alias webapp --name app1 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app2 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app3 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app4 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --network-alias webapp --name app5 --env-file app.env jfahrer/demo_web_app:latest

docker container run -d --network mynet --name lb --env-file lb.env -p 80:80 ewajs/lb:latest