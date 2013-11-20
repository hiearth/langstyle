#!/usr/bin/env python3

import unittest
from langstyle.database import character_repository

class NextTest(unittest.TestCase):

    def setUp(self):
        self._user_id = 1
        self._character_repository = character_repository.CharacterRepository()

    def tearDown(self):
        return super().tearDown()
    
    def test_FirstTime(self):
        # pre condition, no learning record
        first_character = self._character_repository.next(self._user_id)
        # assert first_character 
        self.fail("no assertion yet")

    def test_StartButNotComplete(self):
        # pre condition, has some learning record
        next_character = self._character_repository.next(self._user_id)
        # assert next_character  
        self.fail("no assertion yet")

    def test_Complete(self):
        # pre condition, has full learning record
        complete_signal = self._character_repository.next(self._user_id)
        # assert complete_signal  
        self.fail("no assertion yet")