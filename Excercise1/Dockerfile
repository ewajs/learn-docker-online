FROM debian:buster-slim

RUN apt-get update && apt-get install -y nginx

# Delete nginx's default log file and create a sym link to /dev/stdout for it
# This has the effect of "piping" nginx logs to STDOUT to be retrieved by
# docker container log containerName
RUN rm /var/log/nginx/access.log && ln -s /dev/stdout /var/log/nginx/access.log

# Shell form, will execute the command inside a shell
# with the shell having the PID 1
# CMD nginx -g 'daemon off;'

# Exec form, will execute the command itself giving it
# PID 1
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

