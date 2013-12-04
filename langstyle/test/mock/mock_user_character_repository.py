#!/usr/bin/env python

class MockUserCharacterRepository:

    def __init__(self):
        self._user_grasp = {}
        self._user_learning = {}

    def grasp(self, user_id):
        character_ids = self._user_grasp.get(user_id, [])
        return character_ids.copy()

    def count(self, user_id, character_id):
        pass

    def get_learning(self, user_id):
        learning_characters = self._user_learning.get(user_id, [])
        return [item.character_id for item in learning_characters]

    def get_current_character(self, user_id):
        learning_characters = self._user_learning.get(user_id, [])
        for item in learning_characters:
            if item.is_current:
                return item.character_id
        return None

    def begin_learn(self, user_id, character_id):
        if user_id not in self._user_learning:
            self._user_learning[user_id] = []
        learning_characters = self._user_learning.get(user_id)
        learning_characters.append(_UserLearning(user_id, character_id))

    def _is_in_learning_list(self,user_id, character_id):
        learning_characters = self._user_learning.get(user_id, [])
        for item in learning_characters:
            if item.character_id == character_id:
                return True
        return False

    def set_current_character(self, user_id, character_id):
        learning_characters = self._user_learning.get(user_id, [])
        if not self._is_in_learning_list(user_id,character_id):
            raise Exception("character_id not in learning list")
        for item in learning_characters:
            if item.character_id == character_id:
                item.is_current = True
            else:
                item.is_current = False

    def mark_grasp(self, user_id, character_id):
        if user_id not in self._user_grasp:
            self._user_grasp[user_id] = []
        character_ids = self._user_grasp.get(user_id)
        character_ids.append(character_id)


class _UserLearning:

    def __init__(self, user_id,character_id, repeat_count=0, is_current=False):
        self.user_id = user_id
        self.character_id = character_id
        self.repeat_count = repeat_count
        self.is_current = is_current 