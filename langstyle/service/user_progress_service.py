#!/usr/bin/env python

#import pdb
import random
import datetime
import concurrent.futures
from .. import helper
from .. import config

class UserProgressService:

    def __init__(self, user_progress_repository):
        self._user_progress_repository = user_progress_repository
        self._learning_status = "Learning"
        self._learned_status = "Learned"
        self._known_status = "Known"
        self._review_status = "Review"
        self._grasp_status = "Grasp"

    def next(self, user_id):
        show_candidate_words = self._get_could_show_words(user_id)
        if show_candidate_words:
            word_meaning_service = config.service_factory.get_word_meaning_service()
            return random.choice([word_meaning_service.get(candidate_word.word_meaning_id) 
                    for candidate_word in show_candidate_words])
        return None

        #current_word_meaning_id = self.get_current(user_id)
        #if current_word_meaning_id is not None:
        #    return current_word_meaning_id

    def _get_word_meanings(self, ids):
        word_meaning_service = config.service_factory.get_word_meaning_service()
        return [word_meaning_service.get(id) for id in ids]

    def _need_add_learning_word_meaning(self, learning_count):
        return learning_count < config.MAX_IN_LEARNING_COUNT

    def _add_learning_words(self, user_id, asyn=True):
        try:
            executor = concurrent.futures.ThreadPoolExecutor(1)
            executor.submit(self._add_word_meaning_to_learning_list, user_id)
        except Exception as e:
            config.service_factory.get_log_service().error(str(e))
        finally:
            executor.shutdown(not asyn)

    def _add_word_meaning_to_learning_list(self, user_id):
        unknown_word_meanings = self.get_unknown(user_id)
        # need use a more intelligent class/function to do the next job
        if unknown_word_meanings:
            candidate_word_meaning = random.choice(unknown_word_meanings)
            self._user_progress_repository.begin_learn(user_id, candidate_word_meaning)

    def get(self, user_id, word_meaning_id):
        return self._user_progress_repository.get(user_id, word_meaning_id)

    def get_grasp(self, user_id):
        return self._user_progress_repository.get_grasp(user_id)

    def get_count(self, user_id, word_meaning_id):
        return self._user_progress_repository.get_count(user_id, word_meaning_id)

    def get_learn(self, user_id):
        '''get recent learning word meaning id list'''
        learning_words = self._user_progress_repository.get_learn(user_id)
        if not learning_words:
            self._add_learning_words(user_id, False)
            learning_words = self._user_progress_repository.get_learn(user_id)
        elif self._need_add_learning_word_meaning(len(learning_words)):
            self._add_learning_words(user_id)
        return learning_words

    def get_know(self, user_id):
        return self._user_progress_repository.get_know(user_id)

    def get_known(self, user_id):
        return self._user_progress_repository.get_by_status(user_id, "Known")

    def get_current(self, user_id):
        '''get current learning word meaning id'''
        return self._user_progress_repository.get_current(user_id)

    def get_unknown(self, user_id):
        return self._user_progress_repository.get_unknown(user_id)

    def get_levels(self, user_id):
        return self._user_progress_repository.get_levels(user_id)

    def is_level_complete(self, user_id, level):
        return self._user_progress_repository.is_level_complete(user_id, level)

    def get_word_meanings_of_level(self, user_id,level):
        return self._user_progress_repository.get_word_meanings_of_level(user_id, level)

    def get_review(self, user_id):
        return self._user_progress_repository.get_review(user_id)

    def _get_on_progress_words(self, user_id):
        words = []
        words.extend(self.get_learn(user_id))
        words.extend(self.get_review(user_id))
        return words

    def _get_should_not_show_words(self, user_id):
        words = self._get_on_progress_words(user_id)
        sort_key = (lambda progress_item: progress_item.last_learning_time 
                    if progress_item.last_learning_time else datetime.datetime.min)
        words.sort(key=sort_key)
        if len(words) > config.WORD_SHOW_AGAIN_MIN_INTERVAL:
            return words[-config.WORD_SHOW_AGAIN_MIN_INTERVAL:]
        return []

    def _get_could_show_words(self, user_id):
        progress_words = self._get_on_progress_words(user_id)
        should_not_show = self._get_should_not_show_words(user_id)
        if should_not_show:
            return [word for word in progress_words if word not in should_not_show]
        return progress_words

    def _should_add_review_word(self, user_id):
        return len(self.get_review(user_id)) < config.MAX_REVIEW_COUNT

    def _get_highest_available_level_to_learn(self, user_id):
        learned_levels = self.get_levels(user_id)
        highest_level = max(learned_levels)
        if self.is_level_complete(user_id, highest_level):
            all_levels = self._get_all_levels_to_learn(user_id)
            highest_level = min((level for level in all_levels if level > highest_level))
        return highest_level

    def _get_all_levels_to_learn(self, user_id):
        user_info = config.service_factory.get_user_service().get_by_id(user_id)
        return config.service_factory.get_word_meaning_service().get_levels(user_info.language_map_id)

    def get_status(self, user_id, word_meaning_id):
        return self._user_progress_repository.get_status(user_id, word_meaning_id)

    def update_status(self, user_id, word_meaning_id, is_pass):
        # user progress audit table record user's learning detail
        #pdb.set_trace()
        progress_item = self.get(user_id, word_meaning_id)
        next_status = self._get_next_status(progress_item.status, is_pass, progress_item.last_learning_time)
        self._user_progress_repository.update(user_id, word_meaning_id, next_status)

    def _get_next_status(self, current_status, is_pass, last_learning_time):
        if not is_pass:
            return self._learning_status
        if current_status == self._learning_status and last_learning_time is None:
            return self._known_status
        if current_status == self._learning_status and last_learning_time is not None:
            return self._learned_status
        if current_status == self._learned_status:
            return self._review_status
        if current_status == self._review_status:
            return self._grasp_status
        if current_status == self._known_status:
            return self._grasp_status
        return current_status
