# Excercise 3
(Not exactly excercise 3)
The following docker commands will:
- Create a User Defined Network
- Spin up a Postgres container (configuration passed through `app.env` file).
- Spin up 3 client web servers from the image jfahrer/demo_web_app:latest

The client's image is provided by the course and will create a container that will initiate the database (if not initiated already) and log requests to the web server to the database.

This will create multiple webservers connected to the same database, all logging their requests.

Web servers will be exposed to the host on ports 80, 81 and 82.

```bash
docker network create eze

docker container run -d --env-file app.env --network eze --name db postgres

docker container run -p 80:9292 --env-file app.env --name s1 --network eze jfahrer/demo_web_app

docker container run -p 81:9292 --env-file app.env --name s2 --network eze jfahrer/demo_web_app

docker container run -p 82:9292 --env-file app.env --name s3 --network eze jfahrer/demo_web_app 

```

