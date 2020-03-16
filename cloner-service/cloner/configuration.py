#!/var/cloner-service/virtualenv/bin/python
import glob
import json
import os


class JsonMapper:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @classmethod
    def from_json_str(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    @classmethod
    def from_json_dict(cls, json_dict):
        return cls(**json_dict)


class Dict2Object:
    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)


class Configuration(JsonMapper):
    def __init__(self, manager, host="127.0.0.1", port=5000, log_level="INFO"):
        self.host = host
        self.port = port
        self.log_level = log_level
        self.manager = manager

    def __str__(self):
        return self.to_json()


class Clone(JsonMapper):
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def __str__(self):
        return self.to_json()


def find_config_files(config_dir):
    path = os.path.join(config_dir, "*.json")
    return [os.path.abspath(path) for path in glob.glob(path)]


def load_config_files(config_files):
    configs = []
    for config_file in config_files:
        with open(config_file, encoding='utf-8') as file:
            json_str = file.read()
            try:
                configuration = Configuration.from_json_str(json_str)
                configs.append(configuration)
            except TypeError as type_error:
                print(type_error)

                json_dict = json.loads(json_str)
                if 'clones' in json_dict:
                    for clone in json_dict.get('clones'):
                        configuration = Clone.from_json_dict(clone)
                        configs.append(configuration)
                elif 'clone' in json_dict:
                    configuration = Clone.from_json_dict(json_dict.get('clone'))
                    configs.append(configuration)

    return configs
