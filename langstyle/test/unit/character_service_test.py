#!/usr/bin/env python3

import unittest
from langstyle.service import character_service
from langstyle.database import character_repository
from langstyle.database import repository_context
from langstyle.service import service_context

class NextTest(unittest.TestCase):

    def setUp(self):
        # get a mock user
        self._user_id = 1
        self._character_repository = character_repository.CharacterRepository()
        self._character_service = character_service.CharacterService(self._character_repository)

    def tearDown(self):
        return super().tearDown()

    def test_FirstTime(self):
        # make the user has no learning record
        first_character = self._character_service.next(self._user_id)
        # assert first_character
        self.fail("no assertion yet")

    def test_StartButNotComplete(self):
        # make user has some learning records
        next_character = self._character_service.next(self._user_id)
        # assert next_character
        self.fail("no assertion yet")

    def test_Complete(self):
        # make user has full learning records
        complete_signal = self._character_service.next(self._user_id)
        # assert complete_signal  
        self.fail("no assertion yet")