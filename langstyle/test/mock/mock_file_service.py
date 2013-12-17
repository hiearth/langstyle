#!/usr/bin/env python

class MockFileService:

    def __init__(self):
        self._files = {}

    def read(self, file_name):
        return self._files.get(file_name, None)

    def write(self,file_name, file_data):
        self._files[file_name] = file_data