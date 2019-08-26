# Excercise 10

In this excercise a simple python flask server is built into an image and run inside a container.
A `docker-compose.yml` file is provided besides the `Dockerfile` required to build and run the image in order to provide additional functionality and ease of use.

## Using docker-compose

To build the image and run the container with it's necessary ports exposed is better to use docker-compose. This will also provide the additional functionality of mounting the host's `./app` directory inside the container to override the one built in to facilitate testing the app code.

To start run:

```
docker-compose up
```

The server should be accessible via the host's port 80.

To stop:

```
docker-compose down
```
