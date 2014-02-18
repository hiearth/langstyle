#!/usr/bin/env python

from .. import config
from .. import helper

class CharacterSoundService:

    def __init__(self, character_sound_repository):
        self._character_sound_repository = character_sound_repository

    def get_sounds(self, user_id, character_id):
        custom_sounds = self._character_sound_repository.get_sounds(user_id, character_id)
        if len(custom_sounds) > config.SOUNDS_COUNT_PRE_CHARACTER:
            return custom_sounds[0:config.SOUNDS_COUNT_PRE_CHARACTER]
        return custom_sounds

    def link_exist(self, user_id, character_id, sound_id):
        custom_sounds = self._character_sound_repository.get_sounds(user_id, character_id)
        return sound_id in custom_sounds

    def link(self, user_id, character_id, sound_id):
        if not self.link_exist(user_id, character_id, sound_id):
            self._character_sound_repository.link(user_id, character_id, sound_id)

    def unlink(self, user_id, character_id, sound_id):
        self._character_sound_repository.unlink(user_id, character_id, sound_id)