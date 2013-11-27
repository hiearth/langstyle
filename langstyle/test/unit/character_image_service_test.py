#!/usr/bin/env python

import unittest
from langstyle.service import character_image_service

class CharacterImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._character_image_service = character_image_service.CharacterImageService()


class GetImagesTest(CharacterImageServiceTestCase):
    # _character_image_service.get_images(user_id, character_id)
    pass


class VisualTest(CharacterImageServiceTestCase):
    # bind image to character
    pass

class RemoveTest(CharacterImageServiceTestCase):
    # unbind image
    pass

