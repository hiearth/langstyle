#!/usr/bin/env python

import unittest
from langstyle.service import character_service
from ..mock import mock_character_repository
from .. import test_helper

class CharacterServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._character_repository = mock_character_repository.MockCharacterRepository() 
        self._character_service = character_service.CharacterService(self._character_repository)

    def _get_random_new_character(self, exist_characters):
        return test_helper.generate_character_exclude(exist_characters)

    def _get_random_exist_character(self, exist_characters):
        return test_helper.choice_character(exist_characters)


class AddTest(CharacterServiceTestCase):

    def setUp(self):
        super().setUp()
        # insert some characters to repository
        character_count = 10
        self._added_characters = test_helper.generate_some_characters(character_count)
        for character_item in self._added_characters:
            self._character_repository.add(character_item)


    def test_CharacterIsNew(self):
        new_character = self._get_random_new_character(self._added_characters)
        new_character_id = self._character_service.add(new_character)
        self.assertIsNotNone(new_character_id,"fail to add new character")

    def test_CharacterExist(self):
        word_character = self._get_random_exist_character(self._added_characters)
        character_id = self._character_service.get_id(word_character)
        added_character_id = self._character_service.add(word_character)
        self.assertIsNotNone(added_character_id, "fail to add exist character")
        self.assertEqual(character_id, added_character_id, "duplicate character is added")


class GetTest(CharacterServiceTestCase):

    def test_CharacterExist(self):
        word_character = self._get_random_exist_character(self._added_characters)
        character_id = self._character_service.get_id(word_character)
        self.assertIsNotNone(character_id, "does not find exist character")

    def test_CharacterNotExist(self):
        word_character = self._get_random_new_character(self._added_characters)
        character_id = self._character_service.get_id(word_character)
        self.assertIsNone(character_id, "find non exist character")