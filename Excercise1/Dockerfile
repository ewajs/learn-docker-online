FROM debian:buster-slim

RUN apt-get update && apt-get install -y nginx

# Shell form, will execute the command inside a shell
# with the shell having the PID 1
# CMD nginx -g 'daemon off;'

# Exec form, will execute the command itself giving it
# PID 1
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

