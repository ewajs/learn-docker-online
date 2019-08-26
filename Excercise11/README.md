# Excercise 11

This excercise builds up on what was done in [**Excercise 11**](https://github.com/ewajs/learn-docker-online/tree/master/Excercise10). In this case, no further changes to the image or the `docker-compose.yml` were performed. The app's code is injected into the container at startup via a Bind Volume.

The only addition is that the app now logs Client IP, Path, Container Hostname and Timestamp at each request to a file inside the container located in `/tmp/requests.txt`.

## Starting the Web Server and verifying it runs

To start everything (in daemon mode) run:

```
docker-compose up -d
```

You should be able to connect to the container by accessing port 80 of the container's host.

To verify the requests are being logged you can execute the following command in the container:

```
docker container exec -it CONTAINER_NAME tail -f /tmp/requests.txt
```

Be sure to replace `CONTAINER_NAME` with your container name and to make a request first to ensure the file already exists.
