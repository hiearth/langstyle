#!/usr/bin/env python

import shutil
from . import util
from . import web
from .. import config

class SoundHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self.character = None

    def get(self):
        sound_id = self._get_request_sound()
        sound_content = self._get_service().get(sound_id)
        if sound_content is None:
            self.send_not_found()
            return
        self.send_headers_and_content(sound_content)

    def post(self):
        sound_file = self.get_file()
        sound_id = self._get_service().add(sound_file, self.user_id)
        self.send_headers_and_content(str(sound_id))

    def get_content_type(self):
        return "audio/mpeg"

    def _get_request_sound(self):
        sound_ids = self._get_regex().findall(self.get_path())
        if sound_ids:
            return sound_ids[0]
        return None

    def _get_service(self):
        return config.service_factory.get_sound_service()