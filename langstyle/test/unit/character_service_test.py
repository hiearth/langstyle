#!/usr/bin/env python3

import unittest
from langstyle import service.character

class GetTest(unittest.TestCase):

    def FirstTime_ReturnFirst(self):
        first_character = character.get()
        # assert first_character not None
        #unittest.assert(first_character)
        pass

    def WithPrevious_ReturnNext(self, previous_character):
        next_character = character.get(previous_character)
        # assert next_character 
        pass
