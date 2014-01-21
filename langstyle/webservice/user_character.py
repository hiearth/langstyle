#!/usr/bin/env python

import re
from . import web
from .. import config

class UserCharacterHandler(web.RequestHandler):

    def _get_user_character_service(self):
        return config.service_factory.get_user_character_service()

    def _get_character_service(self):
        return config.service_factory.get_character_service()

    def get_content_type(self):
        return "text/plain"

    def _get_characters_by_ids(self, character_ids):
        character_service = self._get_character_service()
        for character_id in character_ids:
            character = character_service.get(character_id)
            if character:
                yield character

    def _join_characters(characters_iter):
        if not characters_iter:
            return ", ".join(characters_iter)
        return None



class UserCharacterCountHandler(UserCharacterHandler):

    def _get_request_character(self):
        request_path = self.get_path()
        character_regex = re.compile(r"/usercharacter/count/(.*)")
        characters = character_regex.findall(request_path)
        if characters:
            return characters[0]
        return None

    def get(self):
        query_character = self._get_request_character()
        if not query_character:
            self.send_not_found()
            return
        character_service = self._get_character_service()
        character_id = character_service.get_id(query_character)
        if character_id is None:
            self.send_not_found()
            return
        user_character_service = self._get_user_character_service()
        character_count = user_character_service.get_count(self.user_id, character_id)
        self.send_headers_and_content(str(character_count))


class UserCharacterGraspHandler(UserCharacterHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        grasp_characters = self._get_grasp_characters()
        characters_string = self._join_characters(grasp_characters)
        if characters_string:
            self.send_headers_and_content(characters_string)
        else:
            self.send_not_found()

    def _get_grasp_characters(self):
        user_character_service = self._get_user_character_service()
        grasp_character_ids = user_character_service.get_grasp(self.user_id)
        return self._get_characters_by_ids(grasp_character_ids)


class UserCharacterCurrentHandler(UserCharacterHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        current_character = None
        user_character_service = self._get_user_character_service()
        character_id = user_character_service.get_current_character(self.user_id)
        if character_id is None:
            self.send_not_found()
            return
        #character_service = self._get_character_service()
        #current_character = character_service.get(character_id)
        #if not current_character:
        #    self.send_not_found()
        #    return
        #self.send_headers_and_content(current_character)
        # need to return json data
        self.send_headers_and_content(str(character_id))


class UserCharacterLearningHanlder(UserCharacterHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        learning_characters = self._get_learning_characters()
        characters_string = self._join_characters(learning_characters)
        if characters_string:
            self.send_headers_and_content(characters_string)
        else:
            self.send_not_found()

    def _get_learning_characters(self):
        user_character_service = self._get_user_character_service()
        learning_character_ids = user_character_service.get_learning(self.user_id)
        return self._get_characters_by_ids(learning_character_ids)