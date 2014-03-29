#!/usr/bin/env python

from . import base_repository

class LanguageMapRepository(base_repository.BaseRepository):

    def get_id(self, from_id, target_id):
        language_map_id = self._call_proc_query_one("LanguageMap_Id_S", [from_id, target_id])
        if language_map_id:
            return language_map_id[0]
        return None
