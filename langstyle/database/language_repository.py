#!/usr/bin/env python

from . import base_repository

class LanguageRepository(base_repository.BaseRepository):

    def get_id(self, language_name):
        language_id = self._call_proc_query_one("WordLanguage_S_By_Name", [language_name])
        if language_id:
            return language_id[0]
        return None
    
    def get(self, language_id):
        language_name = self._call_proc_query_one("WordLanguage_S", [language_id])
        if language_name:
            return language_name[0]
        return None
