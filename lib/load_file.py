import yaml
import os


class LoadFile:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def read_file(self):
        data_path = os.path.join(self.file_path, self.file_name)
        with open(data_path, 'r', encoding='utf-8') as data_file:
            data_content = data_file.read()
            data = yaml.safe_load(data_content)

        return data
