#!/usr/bin/env python

class UserCharacterService:

    def __init__(self, user_character_repository):
        self._user_character_repository = user_character_repository

    def next(self, user_id):
        learning_list = self.get_learning(user_id)
        current_character = self.get_current_character(user_id)
        return self._get_next_from_list(learning_list, current_character)

    def _get_next_from_list(self, learning_list, current_character):
        next_character = None
        if learning_list:
            current_character_index = helper.try_index(learning_list, current_character)
            if current_character_index >= 0 and current_character_index < len(learning_list):
                return learning_list[current_character_index + 1]
        return next_character

    def get_grasp(self, user_id):
        return self._user_character_repository.grasp(user_id)

    def count(self, user_id, character_id):
        return self._user_character_repository.count(user_id, character_id)

    def get_learning(self, user_id):
        return self._user_character_repository.get_learning(user_id)

    def get_current_character(self, user_id):
        return self._user_character_repository.get_current_character(user_id)