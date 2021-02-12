from flask import Flask
from db import get_oracle_connection



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    get_oracle_connection()

    app.run(host='0.0.0.0', port=8085)


