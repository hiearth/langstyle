#!/usr/bin/env python

class User:

    def __init__(self,user_id=None, user_name=None, password=None):
        self._id = user_id
        self._name = user_name
        self._password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value