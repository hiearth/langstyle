#!/usr/bin/env python

from . import base_repository
from .. import helper

class CharacterSoundRepository(base_repository.BaseRepository):

    def get_sounds(self, user_id, character_id):
        pass

    def link(self, user_id, character_id, sound_id):
        pass

    def unlink(self, user_id, character_id, sound_id):
        pass