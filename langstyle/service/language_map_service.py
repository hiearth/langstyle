#!/usr/bin/env python

from .. import config

class LanguageMapService:

    def __init__(self, language_map_repository):
        self._language_map_repository = language_map_repository

    def get_id(self, from_language, target_language):
        # get language id
        # query language map id
        language_service = config.service_factory.get_language_service()
        from_id = language_service.get_id(from_language)
        target_id = language_service.get_id(target_language)
        language_map_id = self._language_map_repository.get_id(from_id, target_id)
        return language_map_id
