#!/usr/bin/env python

class UserProgressAuditService:

    def __init__(self, user_progress_audit_repository):
        self._user_progress_audit_repository = user_progress_audit_repository

    def get(self, user_id, word_meaning_id):
        return self._user_progress_audit_repository.get(user_id, word_meaning_id)

    def add(self, user_id, word_meaning_id, is_pass):
        result = "Pass" if is_pass else "Fail"
        self._user_progress_audit_repository.add(user_id, word_meaning_id, result)
