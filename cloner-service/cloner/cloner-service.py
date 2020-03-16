#!/var/cloner-service/virtualenv/bin/python

from flask import Flask

from configuration import find_config_files, load_config_files

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello :)'


@app.route('/v1/health')
def status():
    return 'Health of cloning'


@app.route('/v1/clones')
def clones():
    return 'List of clones'


def args():
    import argparse
    parser = argparse.ArgumentParser(prog='Cloner-service')
    parser.add_argument('-config-dir', required=True, help='A directory of configuration files to load.')
    parser.add_argument('-log-file', required=True, help='Redirect all the cloner-service log messages to a file.')
    parser.add_argument('-debug', action='store_true', help='Debug mode.')
    parser.add_argument('-version', action='version', version='%(prog)s v@version@')
    return parser.parse_args()


if __name__ == '__main__':
    ARGS = args()

    config_files = find_config_files(ARGS.config_dir)
    configs = load_config_files(config_files)

    for config in configs:
        print(config)

    print("Routes: {}".format(app.url_map))

    app.run(host='127.0.0.1', port=5000, debug=ARGS.debug)
