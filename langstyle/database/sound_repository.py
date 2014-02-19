#!/usr/bin/env python

from . import base_repository
from ..entity import word_sound

class SoundRepository(base_repository.BaseRepository):

    def get(self, sound_id):
        sound_result = self._call_proc_query_one(
            "WordSound_S_By_Id", [sound_id])
        if sound_result:
            return word_sound.WordSound(
                sound_id, sound_result[0], sound_result[1])
        return None

    def add(self, sound_md5, user_provider_id):
        result = self._call_proc_non_query(
            "WordSound_I", [sound_md5, user_provider_id, None])
        if result:
            return result[2]
        return None