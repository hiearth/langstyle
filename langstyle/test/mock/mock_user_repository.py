#!/usr/bin/env python

class MockUserRepository:

    def __init__(self):
        self._user_grasp = {}
        self._user_learning = {}

    def grasp(self, user_id):
        character_ids = self._user_grasp.get(user_id, [])
        return character_ids.copy()

    def count(self, user_id, character_id):
        pass

    def get_learning(self, user_id):
        character_ids = self._user_learning.get(user_id, [])
        return character_ids.copy()

    def get_current_character(self, user_id):
        pass

    def begin_learn(self, user_id, character_id):
        if user_id not in self._user_learning:
            self._user_learning[user_id] = []
        character_ids = self._user_learning.get(user_id) 
        character_ids.append(character_id)

    def mark_grasp(self, user_id, character_id):
        if user_id not in self._user_grasp:
            self._user_grasp[user_id] = []
        character_ids = self._user_grasp.get(user_id)
        character_ids.append(character_id)