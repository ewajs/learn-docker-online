# Excercise 16

In this excercise a swarm will be created with one manager and two workers. An overlay network will be created, and two services connected to it: one web frontend service and a load balancer service, pointing to the web frontend and exposing it's port 80 to the outside of the cluster. Then, the web frontend service will be scaled to 5 replicas. Lastly, a failed service update will be performed to the web fronted with an automatic rollback. No additional files besides this readme are needed to complete this excercise.

## Intialization of the Swarm

First, manager and workers need to be created, for that, the following commands should be executed in the hosts.

For that, in the designated manager host, run:

```docker
docker swarm init --advertise-addr IP_ADDRESS
```

Where `IP_ADDRESS` should be the IP that's in the same network as the workers (if the host happens to be connected to more than one network). This should output the command that needs to be executed in the workers (once in each one), it should look something like:

```docker
docker swarm join --token SWMTKN-1-0i8cgbqaqbv9tavpl8p83x31bav3sghu98apji8yeuxjvl8iow-9q6hfduds0hnh1rxghci1mbuc 192.168.0.13:2377
```

Once all hosts have been created and joined the swarm, you can verify with:

```docker
docker node ls
```

And it should output all nodes (3 in this case, one manager, two workers).

**All subsequent commands are supposed to be run on the manager node.**

## Creating the Overlay Network

To create an overlay network run:

```docker
docker network create --driver overlay srvnet
```

## Creating the Frontend Service

To create the frontend service run:

```docker
docker service create --name demo-frontend --network srvnet jfahrer/swarm-demo-frontend:v4
```

## Creating the Load Balancer Service

To create the load balancer service run:

```docker
docker service create --name demo-lb --network srvnet --env PROXY_UPSTREAM=demo-frontend:8080 -p 80:80 jfahrer/swarm-demo-lb:v1
```

After this command you should be able to access the frontend via port 80 in the manager's localhost.

## Scaling the Frontend Service

Run:

```docker
docker service update demo-frontend --replicas 5
```

## Performing an Image update with Rollback

Run:

```docker
docker service update --update-failure-action rollback --update-parallelism 3 --update-monitor 10s --image jfahrer/swarm-demo-frontend:v3 demo-frontend
```
