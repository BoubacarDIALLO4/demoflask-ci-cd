from flask import Flask
APP = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    APP.run(host="0.0.0.0")
