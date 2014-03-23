#!/usr/bin/env python

from .. import helper
from . import base_repository

class UserProgressRepository(base_repository.BaseRepository):

    def get_grasp(self, user_id):
        grasp_word_meanings = self._call_proc_query_all("UserProgress_Grasp_S",[user_id])
        return helper.list_comprehension_by_index(grasp_word_meanings, 0)

    def get_count(self, user_id, word_meaning_id):
        result = self._call_proc_query_one("UserProgress_Count_S", [user_id, word_meaning_id])
        if result:
            return result[0]
        return None

    def get_learning(self, user_id):
        learning_word_meanings = self._call_proc_query_all("UserProgress_Learning_S", [user_id])
        return helper.list_comprehension_by_index(learning_word_meanings, 0)

    def get_current(self, user_id):
        result = self._call_proc_query_one("UserProgress_Current_S",[user_id])
        if result:
            return result[0]
        return None

    def get_unknown(self, user_id):
        unknown_word_meanings = self._call_proc_query_all("UserProgress_Unknown_S", [user_id])
        return helper.list_comprehension_by_index(unknown_word_meanings, 0)

    def begin_learn(self, user_id, word_meaning_id):
        self._call_proc_non_query("UserProgress_I", [user_id, word_meaning_id])

    def set_current(self, user_id, word_meaning_id):
        self._call_proc_non_query("UserProgress_Current_U", [user_id, word_meaning_id])

    def increase_count(self, user_id, word_meaning_id):
        self._call_proc_non_query("UserProgress_Count_U", [user_id, word_meaning_id])

    def mark_grasp(self, user_id, word_meaning_id):
        self._call_proc_non_query("UserProgress_Grasp_U", [user_id,word_meaning_id])
