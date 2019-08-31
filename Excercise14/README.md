# Excercise 14

This excercise builds an nginx image and instantiates a container with read only access to it's writable layer and mounting temporary file systems on the paths that the container needs to be able to write on.

## Commands

```
docker image build -t ewajs/nginx:latest .

docker container run -it -p 80:80 --read-only --mount type=tmpfs,dst=/var/lib/nginx/  --mount type=tmpfs,dst=/run/ ewajs/nginx:latest
```
