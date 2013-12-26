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

    def _create_random_file(self):
        random_image = test_helper.generate_mock_image()
        file_md5 = helper.md5_hash(random_image)
        return (file_md5, random_image)

    def _create_non_exist_file(self):
        while True:
            random_file = self._create_random_file()
            file_path = self._file_service.get_file_path(random_file[0])
            if not os.path.exists(file_path):
                return random_file

    def _write_random_new_file(self):
        non_exist_file = self._create_non_exist_file()
        file_path = self._file_service.get_file_path(non_exist_file[0])
        helper.create_dir_if_not_exist(file_path)
        with open(file_path, "wb") as f:
            f.write(non_exist_file[1])
        return non_exist_file[0]


class ReadTest(FileServiceTest):

    def test_FileExist(self):
        file_name = self._write_random_new_file()
        self.assertIsInstance(self._file_service.read(file_name), bytes)

    def test_FileNonExist(self):
        with self.assertRaises(FileNotFoundError):
            self._file_service.read("not_found.file")


class WriteTest(FileServiceTest):

    def test_FileExist(self):
        file_md5 = self._write_random_new_file()
        new_data = test_helper.generate_mock_image()
        self._file_service.write(file_md5, new_data)
        file_path = self._file_service.get_file_path(file_md5)
        written_data = None
        with open(file_path, "rb") as f:
            written_data = f.read()
        self.assertEqual(written_data, new_data)

    def test_FileNonExist(self):
        non_exist_file = self._create_non_exist_file()
        self._file_service.write(non_exist_file[0], non_exist_file[1])
        self.assertTrue(self._file_service.exists(non_exist_file[0]))
