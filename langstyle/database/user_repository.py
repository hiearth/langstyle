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
            return user.User(user_info[0], user_info[1],user_info[2], user_info[3], user_info[4])
        return None

    def get_by_id(self, user_id):
        user_info = self._call_proc_query_one("User_S", [user_id])
        if user_info:
            return user.User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])
        return None

    def update(self, user_id, user_info):
        db_user_info = self._catpure_update_field(user_id,user_info)
        self._call_proc_non_query("User_U", [user_id,db_user_info.email,db_user_info.language_map_id])

    def _catpure_update_field(self,user_id,new_user_info):
        db_user_info = self.get_by_id(user_id)
        if new_user_info.language_map_id is not None:
            db_user_info.language_map_id = new_user_info.language_map_id
        if new_user_info.email is not None:
            db_user_info.email = new_user_info.email
        return db_user_info
