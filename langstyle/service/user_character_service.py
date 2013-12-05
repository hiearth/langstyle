#!/usr/bin/env python

from .. import helper
import random

class UserCharacterService:

    def __init__(self, user_character_repository):
        self._user_character_repository = user_character_repository

    def next(self, user_id):
        learning_ids = self.get_learning(user_id)
        current_character_id = self.get_current_character(user_id)
        if current_character_id is not None:
            return current_character_id
        return self._get_next_from_list(learning_ids)

    # need use a more intelligent class/function to do the next job
    def _get_next_from_list(self, learning_ids):
        if learning_ids:
            return random.choice(learning_ids)
            #current_character_index = helper.try_index(learning_ids, current_character_id)
            #if current_character_index is not None:
            #    return learning_ids[(current_character_index + 1) % len(learning_ids)]
            #else:
            #    return random.choice(learning_ids)
        return None

    def get_grasp(self, user_id):
        return self._user_character_repository.grasp(user_id)

    def count(self, user_id, character_id):
        return self._user_character_repository.count(user_id, character_id)

    def get_learning(self, user_id):
        '''get recent learning character id list'''
        return self._user_character_repository.get_learning(user_id)

    def get_current_character(self, user_id):
        '''get current learning character id'''
        return self._user_character_repository.get_current_character(user_id)