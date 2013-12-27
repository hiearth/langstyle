#!/usr/bin/env python

from . import util
from . import web
from . import character_for_test
from .. import config

class CharacterHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self._character = None
        self._next_character = None

    def _get_service(self):
        return config.service_factory.get_character_service()

    def get(self):
        self._get_service()
        self._character = self._get_character()
        self._get_next()

    def _get_next(self):
        self._next_character = character_for_test.get(self._character)
        self._send_headers()
        self.send_content(self._next_character)

    def _get_character(self):
        return util.get_path_tail(self.get_path())

    def get_content_type(self):
        return character_for_test.get_content_type()

    def get_content_length(self):
        return len(self._next_character)

    def _send_headers(self):
        self.set_response_code(200)
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", self.get_content_length())
        self.send_headers()