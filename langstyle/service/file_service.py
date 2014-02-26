#!/usr/bin/env python

import os
from .. import config
from .. import helper

class FileService:

    def __init__(self, root_dir):
        self._root_dir = root_dir

    def get_file_path(self, file_md5):
        file_relative_path = helper.generate_path_from_md5(file_md5)
        return os.path.join(self._root_dir, file_relative_path)

    def exists(self, file_md5):
        file_path = self.get_file_path(file_md5)
        return os.path.exists(file_path)

    def read(self, file_md5):
        file_path = self.get_file_path(file_md5)
        try:
            with open(file_path, "rb") as f:
                return f.read()
        except FileNotFoundError as e:
            config.service_factory.get_log_service().error(str(e))
        return None

    def write(self, file_md5, file_data):
        file_path = self.get_file_path(file_md5)
        helper.create_dir_if_not_exist(file_path)
        with open(file_path, "wb") as f:
            f.write(file_data)
