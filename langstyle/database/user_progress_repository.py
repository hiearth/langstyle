#!/usr/bin/env python

from .. import helper
from . import base_repository
from ..entity import user_progress

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
        if learning_word_meanings:
            return self._get_progresses(user_id,learning_word_meanings)
        return []

    def get_know(self, user_id):
        know_word_meanings = self._call_proc_query_all("UserProgress_S_By_Status", [user_id, "Know"])
        if know_word_meanings:
            return self._get_progresses(user_id,know_word_meanings)
        return []

    def _get_progresses(self, user_id, progress_list):
        return [user_progress.UserProgress(user_id, learning_item[0], learning_item[1], 
                                            learning_item[2], learning_item[3], learning_item[4]) 
                for learning_item in progress_list]

    def get_current(self, user_id):
        result = self._call_proc_query_one("UserProgress_Current_S",[user_id])
        if result:
            return result[0]
        return None

    def get_review(self, user_id):
        review_word_meanings = self._call_proc_query_all("UserProgress_S_By_Status", [user_id, "Review"])
        if review_word_meanings:
            return self._get_progresses(user_id,review_word_meanings)
        return []

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

    def get_levels(self, user_id):
        levels = self._call_proc_query_all("UserProgress_Levels_S", [user_id])
        return helper.list_comprehension_by_index(levels, 0)

    def is_level_complete(self, user_id, level):
        is_complete = self._call_proc_query_one("UserProgress_Level_Complete", [user_id, level])
        if is_complete:
            return True
        return False

    def get_word_meanings_of_level(self, user_id, level):
        word_ids = self._call_proc_query_all("UserProgress_WordMeanings_S_By_Level", [user_id, level])
        if word_ids:
            return helper.list_comprehension_by_index(word_ids, 0)
        return []