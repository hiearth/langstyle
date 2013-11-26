#!/usr/bin/env python

import unittest
from langstyle.service import character_service
from langstyle.database import character_repository
from ..mock import mock_character_repository

class CharacterServiceTestCase(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._character_repository = mock_character_repository.MockCharacterRepository() 
        self._character_service = character_service.CharacterService(self._character_repository)

    def _get_random_new_character(self):
        raise NotImplementedError()

    def _get_random_exist_character(self):
        raise NotImplementedError()

class AddTest(CharacterServiceTestCase):

    def test_CharacterIsNew(self):
        # make the character repository do not contain this character
        word_character = self._get_random_new_character()
        new_character_id = self._character_service.add(word_character)
        self.assertIsNotNone(new_character_id,"fail to add new character")

    def test_CharacterExist(self):
        word_character = self._get_random_exist_character()
        character_id = self._character_service.get(word_character)
        added_character_id = self._character_service.add(word_character)
        self.assertIsNotNone(added_character_id, "fail to add exist character")
        self.assertEqual(character_id, added_character_id, "duplicate character is added")


class GetTest(CharacterServiceTestCase):

    def test_CharacterExist(self):
        word_character = self._get_random_exist_character()
        character_id = self._character_service.get(word_character)
        self.assertIsNotNone(character_id, "does not find exist character")

    def test_CharacterNotExist(self):
        word_character = self._get_random_new_character()
        character_id = self._character_service.get(word_character)
        self.assertIsNone(character_id, "find non exist character")