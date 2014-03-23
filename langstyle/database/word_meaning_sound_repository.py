#!/usr/bin/env python

from . import base_repository
from .. import helper

class WordMeaningSoundRepository(base_repository.BaseRepository):

    def get_sounds(self, user_id, word_meaning_id):
        custom_sounds = self._call_proc_query_all(
            "WordMeaningSound_Sounds_S", [user_id, word_meaning_id])
        return helper.list_comprehension_by_index(custom_sounds, 0)

    def link(self, user_id, word_meaning_id, sound_id):
        self._call_proc_non_query("WordMeaningSound_I", [user_id, word_meaning_id, sound_id])

    def unlink(self, user_id, word_meaning_id, sound_id):
        self._call_proc_non_query("WordMeaningSound_D", [user_id, word_meaning_id, sound_id])
