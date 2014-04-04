#!/usr/bin/env python

import os

class _RepositoryFactory:
    
    def __init__(self):
        self._character_repository = None
        self._language_map_repository = None
        self._user_character_repository = None
        self._user_progress_repository = None
        self._user_progress_audit_repository = None
        self._word_meaning_image_repository = None
        self._word_meaning_repository = None
        self._word_meaning_sound_repository = None
        self._image_repository = None
        self._sound_repository = None
        self._user_repository = None
        self._language_repository = None
       
    def get_character_repository(self):
        if not self._character_repository:
            from .database import character_repository
            self._character_repository = character_repository.CharacterRepository()
        return self._character_repository

    def get_user_progress_repository(self):
        if not self._user_progress_repository:
            from .database import user_progress_repository
            self._user_progress_repository = user_progress_repository.UserProgressRepository()
        return self._user_progress_repository
    
    def get_user_progress_audit_repository(self):
        if not self._user_progress_audit_repository:
            from .database import user_progress_audit_repository
            self._user_progress_audit_repository = user_progress_audit_repository.UserProgressAuditRepository()
        return self._user_progress_audit_repository

    def get_user_character_repository(self):
        if not self._user_character_repository:
            from .database import user_character_repository
            self._user_character_repository = user_character_repository.UserCharacterRepository()
        return self._user_character_repository

    def get_word_meaning_repository(self):
        if not self._word_meaning_repository:
            from .database import word_meaning_repository 
            self._word_meaning_repository = word_meaning_repository.WordMeaningRepository()
        return self._word_meaning_repository

    def get_word_meaning_image_repository(self):
        if not self._word_meaning_image_repository:
            from .database import word_meaning_image_repository
            self._word_meaning_image_repository = word_meaning_image_repository.WordMeaningImageRepository()
        return self._word_meaning_image_repository

    def get_word_meaning_sound_repository(self):
        if not self._word_meaning_sound_repository:
            from .database import word_meaning_sound_repository
            self._word_meaning_sound_repository = word_meaning_sound_repository.WordMeaningSoundRepository()
        return self._word_meaning_sound_repository

    def get_image_repository(self):
        if not self._image_repository:
            from .database import image_repository
            self._image_repository = image_repository.ImageRepository()
        return self._image_repository

    def get_sound_repository(self):
        if not self._sound_repository:
            from .database import sound_repository
            self._sound_repository = sound_repository.SoundRepository()
        return self._sound_repository

    def get_user_repository(self):
        if not self._user_repository:
            from .database import user_repository
            self._user_repository = user_repository.UserRepository()
        return self._user_repository

    def get_language_repository(self):
        if not self._language_repository:
            from .database import language_repository
            self._language_repository = language_repository.LanguageRepository()
        return self._language_repository

    def get_language_map_repository(self):
        if not self._language_map_repository:
            from .database import language_map_repository
            self._language_map_repository = language_map_repository.LanguageMapRepository()
        return self._language_map_repository


class _ServiceFactory:

    def __init__(self):
        self._language_service = None
        self._language_map_service = None
        self._character_service = None
        self._image_service = None
        self._sound_service = None
        self._user_service = None
        self._user_progress_service = None
        self._user_progress_audit_service = None
        self._word_meaning_service = None
        self._word_meaning_image_service = None
        self._word_meaning_sound_service = None
        self._image_file_service=None
        self._sound_file_service = None
        self._log_service = None

    def get_language_service(self):
        if not self._language_service:
            from .service import language_service
            repository = repository_factory.get_language_repository()
            self._language_service = language_service.LanguageService(repository)
        return self._language_service

    def get_language_map_service(self):
        if not self._language_map_service:
            from .service import language_map_service
            repository = repository_factory.get_language_map_repository()
            self._language_map_service = language_map_service.LanguageMapService(repository)
        return self._language_map_service

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

    def get_user_progress_service(self):
        if not self._user_progress_service:
            from .service import user_progress_service
            repository = repository_factory.get_user_progress_repository()
            self._user_progress_service = user_progress_service.UserProgressService(repository)
        return self._user_progress_service

    def get_user_progress_audit_service(self):
        if not self._user_progress_audit_service:
            from .service import user_progress_audit_service
            repository = repository_factory.get_user_progress_audit_repository()
            self._user_progress_audit_service = user_progress_audit_service.UserProgressAuditService(repository)
        return self._user_progress_audit_service

    def get_word_meaning_service(self):
        if not self._word_meaning_service:
            from .service import word_meaning_service
            repository = repository_factory.get_word_meaning_repository()
            self._word_meaning_service = word_meaning_service.WordMeaningService(repository)
        return self._word_meaning_service

    def get_word_meaning_image_service(self):
        if not self._word_meaning_image_service:
            from .service import word_meaning_image_service
            repository = repository_factory.get_word_meaning_image_repository()
            self._word_meaning_image_service = word_meaning_image_service.WordMeaningImageService(repository)
        return self._word_meaning_image_service

    def get_word_meaning_sound_service(self):
        if not self._word_meaning_sound_service:
            from .service import word_meaning_sound_service
            repository = repository_factory.get_word_meaning_sound_repository()
            self._word_meaning_sound_service = word_meaning_sound_service.WordMeaningSoundService(repository)
        return self._word_meaning_sound_service

    def get_image_service(self):
        if not self._image_service:
            from .service import image_service
            repository = repository_factory.get_image_repository()
            self._image_service = image_service.ImageService(repository, self.get_image_file_service())
        return self._image_service

    def get_sound_service(self):
        if not self._sound_service:
            from .service import sound_service
            repository = repository_factory.get_sound_repository()
            self._sound_service = sound_service.SoundService(repository, self.get_sound_file_service())
        return self._sound_service


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

    def get_user_service(self):
        if not self._user_service:
            from .service import user_service
            repository = repository_factory.get_user_repository()
            self._user_service = user_service.UserService(repository)
        return self._user_service


def _is_openshift():
    openshift_db = os.getenv("OPENSHIFT_MYSQL_DB_HOST")
    if openshift_db:
        return True
    return False

if _is_openshift():
    mysql_host = os.getenv("OPENSHIFT_MYSQL_DB_HOST")
    database_connection = {"user":"admindG4Vp4G",
                           "password":"R2fF-1y2teRd",
                           "host":mysql_host,
                           "database": "langstyle",
                           "raise_on_warnings": True}
else:
    database_connection = {"user":"hiearth", 
                           "password":"hu1987jie", 
                           "host":"localhost", 
                           "database": "langstyle", 
                           "raise_on_warnings": False}


repository_factory = _RepositoryFactory()
service_factory = _ServiceFactory()

ROOT_DIRECTORY = os.path.dirname(__file__)

DATA_DIRECTORY = os.path.abspath(os.path.join(ROOT_DIRECTORY,"..","data"))
IMAGE_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "image")
SOUND_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "sound")

POPULATION_DIRECTORY = os.path.abspath(os.path.join(ROOT_DIRECTORY, "..", "population"))
ENGLISH_POPULATION_DIRECTORY = os.path.join(POPULATION_DIRECTORY, "english")

MAX_IN_LEARNING_COUNT = 7 # need to customize to fit each user
MAX_REVIEW_COUNT = 3
WORD_SHOW_AGAIN_MIN_INTERVAL = 3
IMAGES_COUNT_PER_WORD_MEANING = 20
SOUNDS_COUNT_PRE_WORD_MEANING = 5

_DATABASE_DEFINITION_DIR = os.path.abspath(os.path.join(ROOT_DIRECTORY, "database"))
DATABASE_SCHEMA_DIR = os.path.join(_DATABASE_DEFINITION_DIR, "schema")
DATABASE_PROCEDURE_DIR = os.path.join(_DATABASE_DEFINITION_DIR,"procedure")
DATABASE_PREPOPULATION_DIR = os.path.join(_DATABASE_DEFINITION_DIR, "prepopulation")

ADMINISTRATOR_ID = 1
