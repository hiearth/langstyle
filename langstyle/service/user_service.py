#!/usr/bin/env python

class UserService:

    def __init__(self, user_repository):
        self._user_repository = user_repository

    def add(self, user_name, user_password, email):
        if self.exist(user_name):
            raise Exception("user name already exist")
        return self._user_repository.add(user_name, user_password, email)

    def exist(self, user_name):
        user_info = self.get(user_name)
        return user_info is not None

    def get(self, user_name):
        return self._user_repository.get(user_name)