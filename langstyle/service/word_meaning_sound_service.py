#!/usr/bin/env python

from .. import config
from .. import helper

class WordMeaningSoundService:

    def __init__(self, word_meaning_sound_repository):
        self._word_meaning_sound_repository = word_meaning_sound_repository

    def get_sounds(self, user_id, word_meaning_id):
        custom_sounds = self._word_meaning_sound_repository.get_sounds(user_id, word_meaning_id)
        if len(custom_sounds) > config.SOUNDS_COUNT_PRE_WORD_MEANING:
            return custom_sounds[0:config.SOUNDS_COUNT_PRE_WORD_MEANING]
        return custom_sounds

    def link_exist(self, user_id, word_meaning_id, sound_id):
        custom_sounds = self._word_meaning_sound_repository.get_sounds(user_id, word_meaning_id)
        return sound_id in custom_sounds

    def link(self, user_id, word_meaning_id, sound_id):
        if not self.link_exist(user_id, word_meaning_id, sound_id):
            self._word_meaning_sound_repository.link(user_id, word_meaning_id, sound_id)

    def unlink(self, user_id, word_meaning_id, sound_id):
        self._word_meaning_sound_repository.unlink(user_id, word_meaning_id, sound_id)