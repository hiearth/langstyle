#!/usr/bin/env python3

from .. import config
from .. import helper

class CharacterService:

    def __init__(self,user_repository):
        self._user_repository = user_repository

    def next(self, user_id):
        user_service = config.service_factory.get_user_service()
        learning_list = user_service.get_learning(user_id)
        current_character = user_service.get_current_character(user_id)
        return self._get_next(learning_list, current_character)

    def _get_next(self, learning_list, current_character):
         current_character_index = helper.try_index(learning_list, current_character)
         if current_character_index >= 0 and current_character_index<len(learning_list):
             return learning_list[current_character_index+1]
         return learning_list[0]