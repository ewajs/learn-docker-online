import datetime as dt
from flask import Flask, request
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    client_ip = request.remote_addr
    path = request.path
    hostname = socket.gethostname()
    timestamp = dt.datetime.now()
    log = """
    -------------------------------------
    REQUEST
    -------------------------------------
    Client IP: {}
    Path: {}
    Server Hostname: {}
    Timestamp: {}
    """.format(client_ip, path, hostname, timestamp)
    with open('/tmp/requests.txt', 'a') as f:
        f.write(log)

    return 'Hello from inside Docker, World!'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
