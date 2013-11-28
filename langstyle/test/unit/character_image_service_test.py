#!/usr/bin/env python

import unittest
from langstyle.service import character_image_service

class CharacterImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._character_image_service = character_image_service.CharacterImageService()

    def _get_random_character(self):
        raise NotImplementedError()


class GetImagesTest(CharacterImageServiceTestCase):
    # _character_image_service.get_images(user_id, character_id)

    def test_HasCustomImages(self):
        character_id = self._get_random_character()
        character_images = self._character_image_service.get_images(self._user_id, character_id)
        # assert that images contain custom image(s) in the top
        self.fail("no assertion yet")

    def test_NoCustomImage(self):
        character_id = self._get_random_character()
        character_images = self._character_image_service.get_images(self._user_id, character_id)
        # assert that images does not contain any custom image
        self.fail("no assertion yet")


class VisualTest(CharacterImageServiceTestCase):
    # bind image to character
    pass

class RemoveTest(CharacterImageServiceTestCase):
    # unbind image
    pass

