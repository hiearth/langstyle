#!/usr/bin/env python

from .. import config

class WordMeaningService:

    def __init__(self, word_meaning_repository):
        self._word_meaning_repository = word_meaning_repository

    def get(self, word_meaning_id):
        return self._word_meaning_repository.get(word_meaning_id)

    def get_id(self, character_id, language_map_id, explaination):
        return self._word_meaning_repository.get_id(character_id, language_map_id, explaination)

    def add(self, character_id, language_map_id, explaination, level):
        id = self.get_id(character_id, language_map_id, explaination)
        if not id:
            id = self._word_meaning_repository.add(character_id, language_map_id, explaination, level)
        return id

    def exist(self, character_id, language_map_id, explaination, level):
        id = self.get_id(character_id, language_map_id, explaination)
        return True if id else False

    def get_levels(self, language_map_id):
        return self._word_meaning_repository.get_levels(language_map_id)
