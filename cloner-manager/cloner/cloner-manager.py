#!/var/cloner-manager/virtualenv/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello cloner-manager !'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
