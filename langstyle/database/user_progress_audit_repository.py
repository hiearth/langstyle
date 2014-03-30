#!/usr/bin/env python

from . import base_repository

class UserProgressAuditRepository(base_repository.BaseRepository):

    def get(self, user_id, word_meaning_id):
        pass

    def add(self,user_id, word_meaning_id, result):
        self._call_proc_non_query("UserProgressAudit_I", [user_id, word_meaning_id, result])
