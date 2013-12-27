#!/usr/bin/env python

import os

class _RepositoryFactory:
    
    def __init__(self):
        self._character_repository = None
        self._user_character_repository = None
       
    def get_character_repository(self):
        if not self._character_repository:
            from .database import character_repository
            self._character_repository = character_repository.CharacterRepository()
        return self._character_repository

    def get_user_character_repository(self):
        if not self._user_character_repository:
            from .database import user_character_repository
            self._user_character_repository = user_character_repository.UserCharacterRepository()
        return self._user_character_repository


class _ServiceFactory:

    def __init__(self):
        self._character_service = None
        self._user_character_service = None
        self._log_service = None
        self._image_file_service=None
        self._sound_file_service = None

    def get_log_service(self):
        if not self._log_service:
            from .service import log_service
            self._log_service = log_service.LogService()
        return self._log_service

    def get_character_service(self):
        if not self._character_service:
            from .service import character_service
            repository = repository_factory.get_character_repository()
            self._character_service = character_service.CharacterService(repository)
        return self._character_service

    def get_user_character_service(self):
        if not self._user_character_service:
            from .service import user_character_service
            repository = repository_factory.get_user_character_repository()
            self._user_character_service = user_character_service.UserCharacterService(repository)
        return self._user_character_service

    def get_image_file_service(self):
        if not self._image_file_service:
            from .service import file_service
            self._image_file_service = file_service.FileService(IMAGE_DATA_DIRECTORY)
        return self._image_file_service

    def get_sound_file_service(self):
        if not self._sound_file_service:
            from .service import file_service
            self._sound_file_service = file_service.FileService(SOUND_DATA_DIRECTORY)
        return self._sound_file_service


repository_factory = _RepositoryFactory()
service_factory = _ServiceFactory()

ROOT_DIRECTORY = os.path.dirname(__file__)
DATA_DIRECTORY = os.path.abspath(os.path.join(ROOT_DIRECTORY,"..","data"))
IMAGE_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "image")
SOUND_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "sound")
MAX_IN_LEARNING_COUNT = 50 # need to customize to fit each user
IMAGES_COUNT_PER_CHARACTER = 20

database_connection = {"user": "hiearth", 
                       "password":"hu1987jie", 
                       "host":"localhost", 
                       "database": "langstyle", 
                       "raise_on_warnings": True}

