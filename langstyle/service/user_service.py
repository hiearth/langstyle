#!/usr/bin/env python3

class UserService:

    def __init__(self, user_repository):
        self._user_repository = user_repository

    def grasp(self, user_id):
        return self._user_repository.grasp(user_id)

    def count(self, user_id, character):
        return self._user_repository.count(user_id, character)

    def get_learning(self, user_id):
        return self._user_repository.get_learning(user_id)

    def get_current_character(self, user_id):
        return self._user_repository.get_current_character(user_id)