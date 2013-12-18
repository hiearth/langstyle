#!/usr/bin/env python

class MockCharacterImageRepository:

    def __init__(self):
        self._character_images = {}

    def get_images(self, user_id, character_id):
        images_link_to_character = self._character_images.get(user_id, {})
        return images_link_to_character.get(character_id, [])

    def link(self, user_id, character_id, image_id):
        if user_id not in self._character_images:
            self._character_images[user_id] = {}
        if character_id not in self._character_images[user_id]:
            self._character_images[user_id][character_id] = []
        if image_id not in self._character_images[user_id][character_id]:
            self._character_images[user_id][character_id].append(image_id)

    def unlink(self, user_id,character_id, image_id):
        pass