#!/usr/bin/env python

class User:

    def __init__(self,user_id=None, user_name=None, password=None, email=None, language_map_id=None):
        self.id = user_id
        self.name = user_name
        self.password = password
        self.email = email
        self.language_map_id = language_map_id