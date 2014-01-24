#!/usr/bin/env python

from . import base_repository
from .. import helper

class UserRepository(base_repository.BaseRepository):

    def add(self, user_name, user_password, email):
        userInfo = self._call_proc_non_query("User_I", (user_name, user_password, email, None))
        if userInfo:
            return userInfo[3]
        return None

    def get(self):
        pass