#!/usr/bin/env python

import re
from . import web
from .. import config

class CharacterImagesHandler(web.RequestHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        character_id = self._get_request_character()
        if character_id is None:
            self.send_not_found()
            return
        character_image_service = config.service_factory.get_character_image_service()
        image_ids = character_image_service.get_images(self.user_id, character_id)
        if not image_ids:
            self.send_not_found()
            return
        image_ids_string = self._join_image_ids(image_ids)
        if image_ids_string:
            self.send_headers_and_content(image_ids_string)
        else:
            self.send_not_found()

    def _join_image_ids(self, image_ids_iter):
        if image_ids_iter:
            return ",".join(str(image_id) for image_id in image_ids_iter)
        return None

    def _get_request_character(self):
        characters = self._get_regex().findall(self.get_path())
        if characters:
            try:
                return int(characters[0])
            except ValueError as e:
                self._log_error(str(e))
        return None


class CharacterImageHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self.character_id = None
        self.image_id = None

    def _get_request_character_image(self):
        request_path = self.get_path()
        resources = self._get_regex().findall(request_path)
        if resources:
            try:
                self.character_id = int(resources[0][0])
                self.image_id = int(resources[0][1])
            except ValueError as e:
                self._log_error(str(e))

    def post(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        self._get_request_character_image()
        if (self.character_id is None) or (self.image_id is None):
            self.send_bad_request()
            return
        character_image_service = config.service_factory.get_character_image_service()
        character_image_service.link(self.user_id, self.character_id, self.image_id)
        self.send_success_headers()

    def delete(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        self._get_request_character_image()
        if (self.character_id is None) or (self.image_id is None):
            self.send_bad_request()
            return
        character_image_service = config.service_factory.get_character_image_service()
        character_image_service.unlink(self.user_id, self.character_id, self.image_id)
        self.send_success_headers()
