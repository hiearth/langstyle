#!/usr/bin/env python

from .. import config

class WordMeaningService:

    def __init__(self, word_meaning_repository):
        self._word_meaning_repository = word_meaning_repository

    def get(self, word_meaning_id):
        return self._word_meaning_repository.get(word_meaning_id)

    def get_levels(self, language_map_id):
        return self._word_meaning_repository.get_levels(language_map_id)
