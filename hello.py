from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    """function"""
    return 'Hello, World!'

if __name__ == '__main__':
    APP.route(host="0.0.0.0")
