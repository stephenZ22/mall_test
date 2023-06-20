import yaml
import os


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Settings:
    def __init__(self):
        self.instance = self.get_instance()

    def get_instance(self):
        config_path = os.path.join(os.path.abspath("./config"), "config.yml")

        with open(config_path, 'r', encoding='utf-8') as config_file:
            config_data = config_file.read()
            config = yaml.safe_load(config_data)
        return config

    def baseUrl(self):
        config_instance = self.get_instance()
        base_url = config_instance.get('default').get('base_url')
        return base_url

    def testUrl(self):
        config_instance = self.get_instance()
        test_url = config_instance.get('default').get('test_url')
        return test_url
