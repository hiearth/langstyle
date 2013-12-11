#!/usr/bin/env python

import unittest
from .. import test_helper
from langstyle.service import image_service
from ..mock import mock_image_repository

class ImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._image_repository = mock_image_repository.MockImageRepository()
        self._image_service = image_service.ImageService(self._image_repository)


class GetTest(ImageServiceTestCase):

    def test_ImageIdExist(self):
        # first use repository add a image, and return the id of added image 
        # call get method, compare the added image equal to the got image
        # can treat the image path as true image, for example generate random image file name
        image_data = test_helper.generate_mock_image()
        image_id = self._image_repository.add(image_data)
        got_image_data = self._image_service.get(image_id)
        self.assertEqual(got_image_data, image_data)

    def test_ImageIdNotExist(self):
        pass