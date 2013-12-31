#!/usr/bin/env python

import re
from . import web
from .. import config

class CharacterImageHandler(web.RequestHandler):

    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        character_id = self._get_request_character()
        if not character_id:
            self.send_not_found()
            return
        character_image_service = config.service_factory.get_character_image_service()
        image_ids = character_image_service.get_images(self.user_id, character_id)
        if not image_ids:
            self.send_not_found()
            return
        image_keys = self._get_image_keys_by_ids(image_ids)
        image_keys_string = self._join_image_keys(image_keys)
        if image_keys_string:
            self.send_success_headers()
            self.send_content(image_keys_string)
        else:
            self.send_not_found()

    def _get_image_keys_by_ids(self, image_ids):
        image_service = config.service_factory.get_image_service()
        for image_id in image_ids:
            image_key = image_service.get_key(image_id)
            if image_key:
                yield image_key

    def _join_image_keys(self, image_keys_iter):
        if image_keys_iter:
            return ", ".join(image_keys_iter)
        return None

    def _get_request_character(self):
        request_path = self.get_path()
        character_regex = re.compile(r"/characterimage/(.*)")
        characters = character_regex.findall(request_path)
        if characters:
            try:
                return int(characters[0])
            except ValueError as e:
                self._log_error(str(e))
        return None

    def post(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        character_id = self._get_request_character()
        if not character_id:
            self.send_not_found()
            return
        image_id = self._get_image_id()
        if not image_id:
            self.send_not_found()
            return
        character_image_service = config.service_factory.get_character_image_service()
        character_image_service.link(self.user_id, character_id, image_id)
        self.send_success_headers()

    def _get_image_id(self):
        body = self.get_body()
        image_id = body.get("imageid".encode(), None)
        if image_id:
            return image_id[0].decode()
        return None

    def delete(self):
        pass