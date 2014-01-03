#!/usr/bin/env python

from . import util
from . import web
from .. import config

class CharacterHandler(web.RequestHandler):

    def _get_service(self):
        return config.service_factory.get_character_service()

    def get(self):
        character_id = self._get_request_character()
        if character_id is None:
            self.send_not_found()
            return
        character_service = self._get_service()
        character_code = character_service.get(character_id)
        if character_code is None:
            self.send_not_found()
            return
        self.send_headers_and_content(character_code)

    def _get_request_character(self):
        characters = self._get_regex().findall(self.get_path())
        if characters:
            try:
                return int(characters[0])
            except ValueError as e:
                self._log_error(str(e))
        return None


class CharacterCodeHandler(web.RequestHandler):

    def _get_service(self):
        return config.service_factory.get_character_service()

    def get(self):
        character_code = self._get_request_character_code()
        character_id = self._get_service().get_id(character_code)
        if character_id is None:
            self.send_not_found()
            return
        self.send_headers_and_content(str(character_id))

    def post(self):
        character_code = self._get_request_character_code()
        character_id = self._get_service().add(character_code)
        if character_id is None:
            self.send_error(500, "Fail to add character.")
            return
        self.send_headers_and_content(str(character_id))

    def _get_request_character_code(self):
        character_codes = self._get_regex().findall(self.get_path())
        if character_codes:
            return character_codes[0]
        return None