#!/usr/bin/env python

from . import web
from .. import config
import json

class UserProgressNextHandler(web.RequestHandler):
    
    def get(self):
        word_meaning = config.service_factory.get_user_progress_service().next(self.user_id)
        if word_meaning is None:
            self.send_not_found()
            return
        next_word = {"wordMeaningId": word_meaning.id, 
                     "characterCode": word_meaning.character_code,
                     "explaination": word_meaning.explaination}
        next_word["images"] = config.service_factory.get_word_meaning_image_service().get_images(self.user_id, word_meaning.id)
        next_word["sounds"] = config.service_factory.get_word_meaning_sound_service().get_sounds(self.user_id, word_meaning.id)
        self.send_headers_and_content(json.dumps(next_word))


class CharacterTestHandler(web.RequestHandler):

    def post(self):
        # user progress table update
        word_meaning_id = int(self.get_form_parameter("wordMeaningId"))
        is_pass = self.get_form_parameter("isPass")
        config.service_factory.get_user_progress_audit_service().add(self.user_id, word_meaning_id, is_pass)
        config.service_factory.get_user_progress_service().update_status(self.user_id, word_meaning_id, is_pass)
        self.send_success_headers()


