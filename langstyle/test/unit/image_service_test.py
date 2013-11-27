#!/usr/bin/env python

import unittest
from langstyle.service import image_service
from ..mock import mock_image_repository

class ImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._image_repository = mock_image_repository.MockImageRepository()
        self._image_service = image_service.ImageService(self._image_repository)
        