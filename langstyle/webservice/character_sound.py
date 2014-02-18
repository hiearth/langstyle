#!/usr/bin/env python

import re
from . import web
from .. import config

class CharacterSoundsHandler(web.RequestHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        character_id = self._get_request_character()
        if character_id is None:
            self.send_not_found()
            return
        character_sound_service = config.service_factory.get_character_sound_service()
        sound_ids = character_sound_service.get_sounds(self.user_id, character_id)
        if not sound_ids:
            self.send_not_found()
            return
        sound_ids_string = self._join_sound_ids(sound_ids)
        if sound_ids_string:
            self.send_headers_and_content(sound_ids_string)
        else:
            self.send_not_found()

    def _join_sound_ids(self, sound_ids_iter):
        if sound_ids_iter:
            return ",".join(str(sound_id) for sound_id in sound_ids_iter)
        return None

    def _get_request_character(self):
        characters = self._get_regex().findall(self.get_path())
        if characters:
            try:
                return int(characters[0])
            except ValueError as e:
                self._log_error(str(e))
        return None


class CharacterSoundHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self.character_id = None
        self.sound_id = None

    def _get_request_character_sound(self):
        resources = self._get_regex().findall(self.get_path())
        if resources:
            try:
                self.character_id = int(resources[0][0])
                self.sound_id = int(resources[0][1])
            except ValueError as e:
                self._log_error(str(e))
    
    def post(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        self._get_request_character_sound()
        if (self.character_id is None) or (self.sound_id is None):
            self.send_bad_request()
            return
        character_sound_service = config.service_factory.get_character_sound_service()
        character_sound_service.link(self.user_id, self.character_id, self.sound_id)
        self.send_success_headers()