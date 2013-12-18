#!/usr/bin/env python

import unittest
from langstyle.service import character_image_service
from ..mock import mock_character_image_repository
from .. import test_helper

class CharacterImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._character_image_repository = mock_character_image_repository.MockCharacterImageRepository()
        self._character_image_service = character_image_service.CharacterImageService(self._character_image_repository)
        self._character_images = {}
        self._link_images_to_characters()

    def _link_images_to_characters(self):
        character_count = 10
        image_count = 5
        character_ids = test_helper.generate_some_ids(character_count)
        for character_id in character_ids:
            image_ids = test_helper.generate_some_ids(image_count)
            for image_id in image_ids:
                self._character_image_repository.link(self._user_id,character_id, image_id)
            self._character_images[character_id] = image_ids
    
    def _get_random_exist_character_id(self):
        return test_helper.choice(list(self._character_images.keys()))

    def _get_images_link_to_character(self, character_id):
        return self._character_images.get(character_id, [])



class GetImagesTest(CharacterImageServiceTestCase):

    def test_HasCustomImages(self):
        character_id = self._get_random_character()
        character_images = self._character_image_service.get_images(self._user_id, character_id)
        # assert that images contain custom image(s) in the top
        self.fail("no assertion yet")

    def test_NoCustomImage(self):
        exist_character_id = self._get_random_exist_character_id()
        character_image_ids = self._character_image_service.get_images(self._user_id, exist_character_id)
        images_link_to_character = self._get_images_link_to_character(exist_character_id)
        self.assertCountEqual(character_image_ids, images_link_to_character)


class LinkImageTest(CharacterImageServiceTestCase):
    pass

class UnlinkImageTest(CharacterImageServiceTestCase):
    pass