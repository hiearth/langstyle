#!/usr/bin/env python

import unittest
from langstyle.service import character_image_service
from ..mock import mock_character_image_repository as mock_repository
#from langstyle.database import character_image_repository
from .. import test_helper

class CharacterImageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        _RepositoryClass = mock_repository.MockCharacterImageRepository
        #_RepositoryClass = character_image_repository.CharacterImageRepository
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
            image_ids = self._link_images_to_character(
                self._user_id, character_id)
            self._character_images[character_id] = image_ids

    def _link_images_to_character(self, user_id, character_id):
        image_count = 5
        image_ids = test_helper.generate_some_ids(image_count)
        for image_id in image_ids:
            self._character_image_repository.link(
                user_id, character_id, image_id)
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
        other_user_image_ids = self._get_images_link_to_character(
            exist_character_id)
        custom_images = self._link_images_to_character(
            another_user, exist_character_id)
        images_link_to_character = self._combine_no_dup(
            custom_images, other_user_image_ids)
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

    def test_LinkIsNew(self):
        exist_character_id = self._get_random_exist_character_id()
        exist_images = self._get_images_link_to_character(exist_character_id)
        new_image = test_helper.generate_int_exclude(exist_images)
        self._character_image_service.link(
            self._user_id, exist_character_id, new_image)
        updated_images = self._character_image_repository.get_images(
            self._user_id, exist_character_id)
        self.assertIn(new_image, updated_images)

    def test_LinkAlreadyExist(self):
        exist_character_id = self._get_random_exist_character_id()
        exist_images = self._get_images_link_to_character(exist_character_id)
        already_link_image = test_helper.choice(exist_images)
        self._character_image_service.link(
            self._user_id, exist_character_id, already_link_image)
        updated_images = self._character_image_repository.get_images(
            self._user_id,exist_character_id)
        self.assertCountEqual(updated_images, exist_images)

class UnlinkImageTest(CharacterImageServiceTestCase):

    def test_HasLink(self):
        exist_character_id = self._get_random_exist_character_id()
        exist_images = self._get_images_link_to_character(exist_character_id)
        already_link_image = test_helper.choice(exist_images)
        self._character_image_service.unlink(
            self._user_id, exist_character_id, already_link_image)
        updated_images = self._character_image_repository.get_images(
            self._user_id, exist_character_id)
        self.assertNotIn(already_link_image, updated_images)

    def test_NoLink(self):
        exist_character_id = self._get_random_exist_character_id()
        exist_images = self._get_images_link_to_character(exist_character_id)
        new_image = test_helper.generate_int_exclude(exist_images)
        self._character_image_service.unlink(
            self._user_id, exist_character_id, new_image)
        custom_images = self._character_image_repository.get_images(
            self._user_id, exist_character_id)
        self.assertCountEqual(exist_images, custom_images)
