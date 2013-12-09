#!/usr/bin/env python

from mysql import connector as dbconnector
from . import base_repository

class UserCharacterRepository(base_repository.BaseRepository):

    def get_grasp(self, user_id):
        grasp_characters = self._call_proc_query_all("UserProgress_Grasp_S",[user_id])
        return [grasp_character[0] for grasp_character in grasp_characters]

    def get_count(self, user_id, character_id):
        raise NotImplementedError()

    def get_learning(self, user_id):
        raise NotImplementedError()

    def get_current_character(self, user_id):
        raise NotImplementedError()

    def begin_learn(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_I", [user_id, character_id])

    def set_current_character(self, user_id, character_id):
        raise NotImplementedError()

    def increase_count(self, user_id, character_id):
        raise NotImplementedError()

    def mark_grasp(self, user_id, character_id):
        self._call_proc_non_query("UserProgress_Grasp_U", [user_id,character_id])