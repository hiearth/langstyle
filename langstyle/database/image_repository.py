#!/usr/bin/env python

from . import base_repository

class ImageRepository(base_repository.BaseRepository):

    def get(self, image_id):
        image_result = self._call_proc_query_one("WordImage_S_By_Id", [image_id])
        if image_result:
            return WordImage(image_id, image_result[0], image_result[1])
        return None

    def add(self, image_md5, user_provider_id):
        result = self._call_proc_non_query("WordImage_I", [image_md5, user_provider_id, None])
        if result:
            return result[2]
        return None

class WordImage:

    def __init__(self, id=None, md5=None, user_provider_id=None):
        self._id = id
        self._md5 = md5
        self._user_provider_id = user_provider_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def md5(self):
        return self._md5

    @md5.setter
    def md5(self, value):
        self._md5 = value

    @property
    def user_provider_id(self):
        return self._user_provider_id

    @user_provider_id.setter
    def user_provider_id(self, value):
        self._user_provider_id = value