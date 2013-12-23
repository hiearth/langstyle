#!/usr/bin/env python

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


