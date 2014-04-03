#!/usr/bin/env python

from . import base_repository
from .. import helper
from ..entity import word_meaning

class WordMeaningRepository(base_repository.BaseRepository):

    def get(self, word_meaning_id):
        word_meaning_info = self._call_proc_query_one("WordMeaning_S", [word_meaning_id])
        if word_meaning_info:
            return word_meaning.WordMeaning(word_meaning_info[0], 
                                            word_meaning_info[2].decode("utf-8"), 
                                            word_meaning_info[4], 
                                            word_meaning_info[5])
        return None

    def add(self):
        #todo
        pass

    def get_levels(self, language_map_id):
        all_levels = self._call_proc_query_all("WordMeaning_Levels_S", [language_map_id])
        if all_levels:
            return helper.list_comprehension_by_index(all_levels, 0)
        return []
