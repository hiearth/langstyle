#!/usr/bin/env python

import random
from .. import helper
from .. import config

class UserCharacterService:

    def __init__(self, user_character_repository):
        self._user_character_repository = user_character_repository

    def next(self, user_id):
        learning_ids = self.get_learning(user_id)
        if self._need_supply_learning_character(len(learning_ids)):
            self.add_character_to_learning_list(user_id)
            learning_ids = self.get_learning(user_id)
        #current_character_id = self.get_current_character(user_id)
        #if current_character_id is not None:
        #    return current_character_id
        return self._get_next_from_list(learning_ids)

    # need use a more intelligent class/function to do the next job
    def _get_next_from_list(self, learning_ids):
        if learning_ids:
            return random.choice(learning_ids)
        return None

    def _need_supply_learning_character(self, learning_count):
        return learning_count < config.MAX_IN_LEARNING_COUNT

    def add_character_to_learning_list(self, user_id):
        unknown_characters = self.get_unknown_characters(user_id)
        # need use a more intelligent class/function to do the next job
        if unknown_characters:
            candidate_character = random.choice(unknown_characters)
            self._user_character_repository.begin_learn(user_id, candidate_character)

    def get_grasp(self, user_id):
        return self._user_character_repository.get_grasp(user_id)

    def get_count(self, user_id, character_id):
        return self._user_character_repository.get_count(user_id, character_id)

    def get_learning(self, user_id):
        '''get recent learning character id list'''
        return self._user_character_repository.get_learning(user_id)

    def get_current_character(self, user_id):
        '''get current learning character id'''
        return self._user_character_repository.get_current_character(user_id)

    def get_unknown_characters(self, user_id):
        return self._user_character_repository.get_unknown_characters(user_id)