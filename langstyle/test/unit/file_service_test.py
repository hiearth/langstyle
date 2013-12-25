#!/usr/bin/env python

import os
import unittest
from langstyle.service import file_service
from langstyle import helper
from .. import test_helper

class FileServiceTest(unittest.TestCase):

    def setUp(self):
        self._data_dir = test_helper.get_image_data_directory()
        self._file_service = file_service.FileService(self._data_dir)


class ReadTest(FileServiceTest):

    def test_FileExist(self):
        file_name = test_helper.create_random_new_file(self._data_dir)
        self.assertIsInstance(self._file_service.read(file_name), bytes)

    def test_FileNonExist(self):
        non_exist_file = os.path.join(self._data_dir, "not_found.file")
        with self.assertRaises(FileNotFoundError):
            self._file_service.read(non_exist_file)

class WriteTest(FileServiceTest):

    def test_FileExist(self):
        file_name = test_helper.create_random_new_file(self._data_dir)
        new_data = test_helper.generate_mock_image()
        self._file_service.write(file_name, new_data)
        written_data = None
        with open(os.path.join(self._data_dir, file_name), "rb") as f:
            written_data = f.read()
        self.assertEqual(written_data, new_data)

    def _create_non_exist_file(self):
        random_image = test_helper.generate_mock_image()
        file_name = helper.md5_hash(random_image)
        while self._file_service.exists(file_name):
            file_name = helper.md5_hash(test_helper.generate_mock_image())
        return file_name

    def test_FileNonExist(self):
        random_image = test_helper.generate_mock_image()
        file_name = self._create_non_exist_file()
        self._file_service.write(file_name, random_image)
        self.assertTrue(self._file_service.exists(file_name))
