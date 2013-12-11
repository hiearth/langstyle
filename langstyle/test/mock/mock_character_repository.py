#!/usr/bin/env python

class MockCharacterRepository:

    def __init__(self):
        self._characters = []

    def add(self, word_character):
        self._characters.append(word_character)
        return len(self._characters) - 1

    def get(self, character_id):
        if (character_id is not None 
            and character_id >=0 
            and character_id < len(self._characters)):
            return self._characters[character_id]
        return None

    def get_id(self, word_character):
        try:
            return self._characters.index(word_character)
        except ValueError:
            return None
