#!/usr/bin/env python

import os
from .. import helper

class FileService:

    def __init__(self, root_dir):
        self._root_dir = root_dir

    def _get_full_path(self, file_path):
        return os.path.join(self._root_dir, file_path)

    def exists(self, file_path):
        return os.path.exists(self._get_full_path(file_path))

    def read(self, file_path):
        full_path = self._get_full_path(file_path)
        with open(full_path, "rb") as f:
            return f.read()

    def _create_dir_if_not_exist(self, full_path):
        owner_dir = os.path.dirname(full_path)
        if not os.path.exists(owner_dir):
            os.makedirs(owner_dir)

    def write(self, file_path, file_data):
        full_path = self._get_full_path(file_path)
        helper.create_dir_if_not_exist(full_path)
        with open(full_path, "wb") as f:
            f.write(file_data)
