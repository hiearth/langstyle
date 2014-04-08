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
                                            word_meaning_info[4].decode("utf-8"), 
                                            word_meaning_info[5])
        return None

    def get_id(self, character_id, language_map_id, explaination):
        word_meaning_id = self._call_proc_query_one("WordMeaning_Id_S",
                                                    [character_id, language_map_id, explaination])
        if word_meaning_id:
            return word_meaning_id[0]
        return None

    def add(self,character_id, language_map_id, explaination, level):
        result = self._call_proc_non_query("WordMeaning_I", [character_id, language_map_id, explaination, level, None])
        return result[4] if result else None

    def get_levels(self, language_map_id):
        all_levels = self._call_proc_query_all("WordMeaning_Levels_S", [language_map_id])
        if all_levels:
            return helper.list_comprehension_by_index(all_levels, 0)
        return []

    def get_by_level(self,language_map_id, level):
        word_meanings = self._call_proc_query_all("WordMeaning_S_By_Level",[language_map_id, level])
        return [word_meaning.WordMeaning(item[0],item[1].decode("utf-8"),item[2].decode("utf-8"),level) 
                for item in word_meanings]

