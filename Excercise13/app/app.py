import datetime as dt
from flask import Flask, render_template, request
from os import getenv
import psycopg2
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    conn_data = {
        'dbname': getenv('POSTGRES_DB'),
        'user': getenv('POSTGRES_USER'),
        'password': getenv('POSTGRES_PASSWORD'),
        'host': getenv('POSTGRES_HOST')
    }

    client_ip = request.remote_addr
    path = request.path
    hostname = socket.gethostname()
    timestamp = dt.datetime.now()

    with psycopg2.connect(**conn_data) as conn:
        with conn.cursor() as c:
            c.execute("""INSERT INTO requests (ip, path, host, requested_at)
            VALUES (%s, %s, %s, %s);""", (client_ip, path, hostname, timestamp))

        with conn.cursor() as c:
            c.execute("""SELECT ip, path, host, requested_at 
                        FROM requests 
                        ORDER BY id DESC
                        LIMIT 25;""")
            reqs = c.fetchall()

    return render_template("index.html", reqs=reqs)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
