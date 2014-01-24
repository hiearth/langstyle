#!/usr/bin/env python

class UserService:

    def __init__(self, user_repository):
        self._user_repository = user_repository

    def add(self, user_name, user_password, email):
        return self._user_repository.add(user_name, user_password, email)

    def exist(self):
        pass

    def get(self):
        pass