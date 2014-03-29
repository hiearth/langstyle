#!/usr/bin/env python

class LanguageService:

    def __init__(self, language_repository):
        self._language_repository = language_repository

    def get_id(self, language_name):
        return self._language_repository.get_id(language_name)

    def get(self, language_id):
        return self._language_repository.get(language_id)
