#!/usr/bin/env python

from . import base_repository
from .. import helper
from ..entity import user

class UserRepository(base_repository.BaseRepository):

    def add(self, user_name, user_password, email):
        userInfo = self._call_proc_non_query("User_I", (user_name, user_password, email, None))
        if userInfo:
            return userInfo[3]
        return None

    def get(self, user_name):
        user_info = self._call_proc_query_one("User_S_By_Name", [user_name])
        if user_info:
            return user.User(user_info[0], user_info[1],user_info[2])
        return None