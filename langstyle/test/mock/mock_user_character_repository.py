#!/usr/bin/env python

import datetime

class MockUserCharacterRepository:

    def __init__(self):
        self._user_progress = {}

    def get_grasp(self, user_id):
        get_by_grasp = (lambda item: item.grasp_time is not None)
        grasp_characters = self._get_characters(user_id,get_by_grasp)
        return [char_item.character_id for char_item in grasp_characters]

    def get_count(self, user_id, character_id):
        character_item = self._get_character_by_id(user_id, character_id)
        if character_item is not None:
            return character_item.repeat_count

    def get_learning(self, user_id):
        progress_characters = self._user_progress.get(user_id,[])
        return [item.character_id for item in progress_characters
                if item.grasp_time is None]

    def get_current_character(self, user_id):
        get_by_is_current = (lambda item: item.is_current == True)
        current_character = self._get_first_character(user_id, get_by_is_current)
        if current_character:
            return current_character.character_id
        return None

    def begin_learn(self, user_id, character_id):
        if user_id not in self._user_progress:
            self._user_progress[user_id] = []
        progress_characters = self._user_progress.get(user_id)
        progress_characters.append(_UserProgress(user_id, character_id))

    def _get_characters(self, user_id, filter_fn):
        filtered_characters = []
        progress_characters = self._user_progress.get(user_id, [])
        for item in progress_characters:
            if filter_fn(item):
                filtered_characters.append(item)
        return filtered_characters

    def _get_first_character(self, user_id, filter_fn):
        '''return first found character, if not found return None'''
        progress_characters = self._user_progress.get(user_id, [])
        for item in progress_characters:
            if filter_fn(item):
                return item
        return None

    def _get_character_by_id(self, user_id, character_id):
        get_by_character_id = (lambda item: item.character_id == character_id)
        return self._get_first_character(user_id, get_by_character_id)

    def _is_in_progress_list(self, user_id, character_id):
        character_item = self._get_character_by_id(user_id, character_id)
        return character_item is not None

    def set_current_character(self, user_id, character_id):
        if not self._is_in_progress_list(user_id, character_id):
            raise Exception("character_id not in progress list")
        progress_characters = self._user_progress.get(user_id, [])
        for item in progress_characters:
            if item.character_id == character_id:
                item.is_current = True
            else:
                item.is_current = False

    def increase_count(self, user_id, character_id):
        if not self._is_in_progress_list(user_id, character_id):
            raise Exception("character_id not in progress list")
        progress_character = self._get_character_by_id(user_id, character_id)
        progress_character.repeat_count += 1

    def mark_grasp(self, user_id, character_id):
        if not self._is_in_progress_list(user_id, character_id):
            raise Exception("character_id not in progress list")
        grasp_character = self._get_character_by_id(user_id, character_id)
        grasp_character.grasp_time = datetime.datetime.today()


class _UserProgress:

    def __init__(self, user_id,character_id, repeat_count=0, 
                 is_current=False, last_learning_time=None, grasp_time=None):
        self.user_id = user_id
        self.character_id = character_id
        self.repeat_count = repeat_count
        self.is_current = is_current
        self.last_learning_time = last_learning_time 
        self.grasp_time = grasp_time
