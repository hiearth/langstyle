#!/usr/bin/env python

import unittest
from langstyle.service import character_image_service
from ..mock import mock_character_image_repository as mock_repository
from .. import test_helper

class CharacterImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        _RepositoryClass = mock_repository.MockCharacterImageRepository
        _ServiceClass = character_image_service.CharacterImageService
        self._character_image_repository = _RepositoryClass()
        self._character_image_service = _ServiceClass(
            self._character_image_repository)
        self._character_images = {}
        self._link_images_to_characters()

    def _link_images_to_characters(self):
        character_count = 10
        image_count = 5
        character_ids = test_helper.generate_some_ids(character_count)
        for character_id in character_ids:
            image_ids = self._link_images_to_character(self._user_id, character_id)
            self._character_images[character_id] = image_ids

    def _link_images_to_character(self, user_id, character_id):
        image_count = 5
        image_ids = test_helper.generate_some_ids(image_count)
        for image_id in image_ids:
            self._character_image_repository.link(user_id, character_id, image_id)
        return image_ids

    def _get_exist_character_ids(self):
        return list(self._character_images.keys())
    
    def _get_random_exist_character_id(self):
        return test_helper.choice(self._get_exist_character_ids())

    def _get_random_new_character_id(self):
        return test_helper.generate_int_exclude(
            self._get_exist_character_ids())

    def _get_images_link_to_character(self, character_id):
        return self._character_images.get(character_id, [])

    def _combine_no_dup(self, one_ids, another_ids):
        exclude_from_one = [id for id in another_ids if id not in one_ids]
        one_ids.extend(exclude_from_one)
        return one_ids



class GetImagesTest(CharacterImageServiceTestCase):

    def test_AllCustomImages(self):
        exist_character_id = self._get_random_exist_character_id()
        character_image_ids = self._character_image_service.get_images(
            self._user_id, exist_character_id)
        images_link_to_character = self._get_images_link_to_character(
            exist_character_id)
        self.assertCountEqual(character_image_ids, images_link_to_character)

    def test_PartialCustomImages(self):
        another_user = 2
        exist_character_id = self._get_random_exist_character_id()
        other_user_image_ids = self._get_images_link_to_character(exist_character_id)
        custom_images = self._link_images_to_character(another_user, exist_character_id)
        images_link_to_character = self._combine_no_dup(custom_images, other_user_image_ids)
        character_image_ids = self._character_image_service.get_images(
            another_user, exist_character_id)
        self.assertCountEqual(character_image_ids, images_link_to_character)

    def test_NoCustomImage(self):
        another_user = 2
        exist_character_id = self._get_random_exist_character_id()
        character_image_ids = self._character_image_service.get_images(
            another_user, exist_character_id)
        images_link_to_character = self._get_images_link_to_character(
            exist_character_id)
        self.assertCountEqual(character_image_ids, images_link_to_character)


class LinkImageTest(CharacterImageServiceTestCase):
    pass

class UnlinkImageTest(CharacterImageServiceTestCase):
    pass
