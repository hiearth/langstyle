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

    def add(self):
        #todo
        pass
