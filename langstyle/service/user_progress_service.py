#!/usr/bin/env python

import random
from .. import helper
from .. import config

class UserProgressService:

    def __init__(self, user_progress_repository):
        self._user_progress_repository = user_progress_repository

    def next(self, user_id):
        learning_ids = self.get_learning(user_id)
        if self._need_add_learning_word_meaning(len(learning_ids)):
            self._add_word_meaning_to_learning_list(user_id)
            learning_ids = self.get_learning(user_id)
        #current_word_meaning_id = self.get_current(user_id)
        #if current_word_meaning_id is not None:
        #    return current_word_meaning_id
        return self._get_next_from_list(learning_ids)

    # need use a more intelligent class/function to do the next job
    def _get_next_from_list(self, learning_ids):
        if learning_ids:
            word_meanings = self._get_word_meanings(learning_ids)
            return random.choice(word_meanings)
        return None

    def _get_word_meanings(self, ids):
        word_meaning_service = config.service_factory.get_word_meaning_service()
        return [word_meaning_service.get(id) for id in ids]

    def _need_add_learning_word_meaning(self, learning_count):
        return learning_count < config.MAX_IN_LEARNING_COUNT

    def _add_word_meaning_to_learning_list(self, user_id):
        unknown_word_meanings = self.get_unknown(user_id)
        # need use a more intelligent class/function to do the next job
        if unknown_word_meanings:
            candidate_word_meaning = random.choice(unknown_word_meanings)
            self._user_progress_repository.begin_learn(user_id, candidate_word_meaning)

    def get_grasp(self, user_id):
        return self._user_progress_repository.get_grasp(user_id)

    def get_count(self, user_id, word_meaning_id):
        return self._user_progress_repository.get_count(user_id, word_meaning_id)

    def get_learning(self, user_id):
        '''get recent learning word meaning id list'''
        return self._user_progress_repository.get_learning(user_id)

    def get_current(self, user_id):
        '''get current learning word meaning id'''
        return self._user_progress_repository.get_current(user_id)

    def get_unknown(self, user_id):
        return self._user_progress_repository.get_unknown(user_id)


def choose_next():
    # get_could_show_words
    # choose one from word list
    pass

def get_learning():
    pass

def get_review():
    pass

def get_should_not_show_words():
    # words that learned in last config.CROSS_WORDS_COUNT_SHOW_AGAIN_AFTER_LEARN
    # words that in the top config.CROSS_WORDS_COUNT_SHOW_AGAIN_AFTER_LEARN order by learned time desc;
    pass

def get_could_show_words():
    # get all learning and review words
    # exclude the should not show words
    pass

def should_add_learning_word():
    # learning words count less than max in-learning count
    pass

def should_add_review_word():
    # review words count less than max review count
    pass

def get_lowest_level_to_learn():
    pass

def get_all_levels_to_learn():
    pass

def get_words_of_level(level):
    pass