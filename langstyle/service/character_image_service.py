#!/usr/bin/env python

class CharacterImageService:

    def get_images(self, user_id, character_id):
        raise NotImplementedError()

    def visual(self, user_id, character_id, image_id):
        raise NotImplementedError()

    def remove(self, user_id, character_id, image_id):
        raise NotImplementedError()