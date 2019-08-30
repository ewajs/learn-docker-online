FROM python:3.6-alpine

WORKDIR /app

COPY /app .

# Add necessary dependencies to run psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install -r requirements.txt \
    && apk del build-deps

EXPOSE 80

CMD ["python", "app.py"]