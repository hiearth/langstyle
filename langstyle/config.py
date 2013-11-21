#!/usr/bin/env python3

import os
from . import database
from . import service

class _RepositoryFactory:
    
    def __init__(self):
        self._character_repository = None
        self._user_repository = None
       
    def get_character_repository(self):
        if not self._character_repository:
            self._character_repository = database.character_repository.CharacterRepository()
        return self._character_repository

    def get_user_repository(self):
        if not self._user_repository:
            self._user_repository = database.user_repository.UserRepository()
        return self._user_repository


class _ServiceFactory:

    def __init__(self):
        self._character_service = None
        self._user_service = None
        self._log_service = None

    def get_log_service(self):
        if not self._log_service:
            self._log_service = service.log_service.LogService()
        return self._log_service

    def get_character_service(self):
        if not self._character_service:
            self._character_service = service.character_service.CharacterService(repository_factory.get_character_repository())
        return self._character_service

    def get_user_service(self):
        if not self._user_service:
            self._user_service = service.user_service.UserService(repository_factory.get_user_repository())
        return self._user_service


repository_factory = _RepositoryFactory()
service_factory = _ServiceFactory()

ROOT_DIRECTORY = os.path.dirname(__file__)
DATA_DIRECTORY = os.path.abspath(os.path.join(ROOT_DIRECTORY,"..","data"))
MAX_IN_LEARNING_COUNT = 50 # need to customize to fit each user

database_connection = {"user": "hiearth", 
                       "password":"hu1987jie", 
                       "host":"localhost", 
                       "database": "langstyle", 
                       "raise_on_warnings": True}

