#!/usr/bin/env python

from . import web
from .. import config
import json

class UserProgressNextHandler(web.RequestHandler):
    
    def get(self):
        if not self.has_permission():
            self.send_access_denied()
            return
        character_id = config.service_factory.get_user_character_service().next(self.user_id)
        if character_id is None:
            self.send_not_found()
            return
        next_word = {"characterId": character_id}
        next_word["characterCode"] = config.service_factory.get_character_service().get(character_id)
        next_word["images"] = config.service_factory.get_character_image_service().get_images(self.user_id, character_id)
        next_word["sounds"] = config.service_factory.get_character_sound_service().get_sounds(self.user_id, character_id)
        self.send_headers_and_content(json.dumps(next_word))