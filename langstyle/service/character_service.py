#!/usr/bin/env python

from .. import config
from .. import helper

class CharacterService:

    def __init__(self,user_repository):
        self._user_repository = user_repository

    def add(self, word_character):
        character_id = self.get_id(word_character)
        if character_id is not None:
            return character_id
        return self._user_repository.add(word_character)

    def get_id(self, word_character):
        return self._user_repository.get_id(word_character)

    def exist(self, word_character):
        character_id = self.get_id(word_character)
        return character_id is not None

    def get(self, character_id):
        return self._user_repository.get(character_id)