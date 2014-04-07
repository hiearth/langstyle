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

    def get_learn(self, user_id):
        learning_word_meanings = self._call_proc_query_all("UserProgress_Learn_S", [user_id])
        if learning_word_meanings:
            return self._get_progresses(user_id,learning_word_meanings)
        return []

    def get_by_status(self, user_id,status):
        word_meanings = self._call_proc_query_all("UserProgress_S_By_Status", [user_id, status])
        if word_meanings:
            return self._get_progresses(user_id, word_meanings)
        return []

    def _get_progresses(self, user_id, progress_list):
        return [user_progress.UserProgress(user_id, item[0], item[1], item[2], item[3], item[4])
                for item in progress_list]

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

    def get_all_unknown(self, user_id):
        unknown_word_meanings = self._call_proc_query_all("UserProgress_Unknown_S", [user_id])
        return helper.list_comprehension_by_index(unknown_word_meanings, 0)

    def get_unknown(self, user_id, level):
        unknown_word_meanings = self._call_proc_query_all("UserProgress_Unknown_In_Level_S", [user_id, level])
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
        if is_complete and is_complete[0]:
            return True
        return False

    def get_word_meanings_of_level(self, user_id, level):
        word_ids = self._call_proc_query_all("UserProgress_WordMeanings_S_By_Level", [user_id, level])
        if word_ids:
            return helper.list_comprehension_by_index(word_ids, 0)
        return []

    def get(self, user_id, word_meaning_id):
        progress = self._call_proc_query_one("UserProgress_S", [user_id, word_meaning_id])
        if progress:
            return user_progress.UserProgress(user_id, word_meaning_id, progress[0], progress[1], progress[2], progress[3])
        return None

    def update(self, user_id, word_meaning_id, status):
        self._call_proc_non_query("UserProgress_U", [user_id, word_meaning_id, status])
