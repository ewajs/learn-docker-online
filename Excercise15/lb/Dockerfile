FROM ewajs/nginx:latest

ENV PROXY_PROTOCOL=http PROXY_UPSTREAM=example.com
RUN apt-get update && apt-get install gettext-base
COPY proxy.conf /etc/nginx/sites-available/default.template
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
