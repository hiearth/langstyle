#!/usr/bin/env python

class CharacterImageService:

    def __init__(self, character_image_repository):
        self._character_image_repository = character_image_repository

    def get_images(self, user_id, character_id):
        return self._character_image_repository.get_images(user_id, character_id)

    def link(self, user_id, character_id, image_id):
        raise NotImplementedError()

    def unlink(self, user_id, character_id, image_id):
        raise NotImplementedError()