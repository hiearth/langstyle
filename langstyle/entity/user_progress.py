#!/usr/bin/env python

import datetime
class UserProgress:

    def __init__(self, user_id=None, word_meaning_id=None, 
                 repeat_count=None, is_current=False, status=None, 
                 last_learning_time=None):
        self.user_id=user_id
        self.word_meaning_id = word_meaning_id
        self.repeat_count=repeat_count
        self.is_current = is_current
        self.status = status
        self._last_learning_time = last_learning_time

    @property
    def last_learning_time(self):
        if not self._last_learning_time:
            return datetime.datetime.min

    @last_learning_time.setter
    def last_learning_time(self, value):
        self._last_learning_time = value
