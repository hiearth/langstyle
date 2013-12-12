#!/usr/bin/env python

from mysql import connector as dbconnector
from .. import helper
from . import base_repository

class UserCharacterRepository(base_repository.BaseRepository):

    def get_grasp(self, user_id):
        grasp_characters = self._call_proc_query_all("UserProgress_Grasp_S",[user_id])
        return helper.list_comprehension_by_index(grasp_characters, 0)

    def get_count(self, user_id, character_id):
        return self._call_proc_query_one("UserProgress_Count_S", [user_id, character_id])

    def get_learning(self, user_id):
        learning_characters = self._call_proc_query_all("UserProgress_Learning_S", [user_id])
        return helper.list_comprehension_by_index(learning_characters, 0)

    def get_current_character(self, user_id):
        return self._call_proc_query_one("UserProgress_Current_S",[user_id])

    def begin_learn(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_I", [user_id, character_id])

    def set_current_character(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_Current_U", [user_id, character_id])

    def increase_count(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_Count_U", [user_id, character_id])

    def mark_grasp(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_Grasp_U", [user_id,character_id])