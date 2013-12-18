#!/usr/bin/env python

import unittest
from langstyle.service import image_service
from langstyle import helper
from .. import test_helper
from ..mock import mock_image_repository
from ..mock import mock_file_service
from langstyle.database import image_repository

class ImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._image_repository = mock_image_repository.MockImageRepository()
        #self._image_repository = image_repository.ImageRepository()
        self._image_file_service = mock_file_service.MockFileService()
        self._image_service = image_service.ImageService(self._image_repository, self._image_file_service)
        self._added_images = []
        self._add_some_images()

    def _add_some_images(self):
        image_count = 10
        images_data = test_helper.generate_some_mock_images(image_count)
        for image_data in images_data:
            self._add_image(image_data)

    def _add_image(self,image_data):
        image_md5 = helper.md5_hash_str(image_data)
        image_id = self._image_repository.add(image_md5, self._user_id)
        self._image_file_service.write(image_md5, image_data)
        self._added_images.append((image_id, image_md5, image_data))
        return image_id

    def _get_random_new_image(self):
        exist_images = helper.list_comprehension_by_index(self._added_images, 2)
        return test_helper.generate_mock_image_exclude(exist_images)

    def _get_exist_image_ids(self):
        return helper.list_comprehension_by_index(self._added_images, 0)

    def _get_random_exist_image_id(self):
        return test_helper.choice(self._get_exist_image_ids())


class GetTest(ImageServiceTestCase):

    def test_ImageIdExist(self):
        image_data = self._get_random_new_image()
        image_id = self._add_image(image_data)
        got_image_data = self._image_service.get(image_id)
        self.assertEqual(got_image_data, image_data)

    def test_ImageIdNotExist(self):
        exist_ids = self._get_exist_image_ids()
        non_exist_id = test_helper.generate_int_exclude(exist_ids)
        non_exist_image = self._image_service.get(non_exist_id)
        self.assertIsNone(non_exist_image)


class AddTest(ImageServiceTestCase):
    
    def test_ImageIsNew(self):
        image_data = test_helper.generate_mock_image()
        image_id = self._image_service.add(image_data, self._user_id)
        self.assertIsNotNone(image_id)