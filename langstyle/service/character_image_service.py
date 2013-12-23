#!/usr/bin/env python

from .. import config

class CharacterImageService:

    def __init__(self, character_image_repository):
        self._character_image_repository = character_image_repository

    def _additional_image_count(self, available_images):
        available_image_count = len(available_images)
        if available_image_count >= config.IMAGES_COUNT_PER_CHARACTER:
            return 0
        return config.IMAGES_COUNT_PER_CHARACTER - available_image_count

    def _not_enough_custom_images(self, custom_images):
        return len(custom_images) < config.IMAGES_COUNT_PER_CHARACTER

    def get_images(self, user_id, character_id):
        images = []
        custom_images = self._character_image_repository.get_images(user_id, character_id)
        additional_image_count = self._additional_image_count(custom_images)
        if additional_image_count > 0:
            additional_images = self._character_image_repository.get_most_used_images(
                character_id, additional_image_count, custom_images)
            custom_images.extend(additional_images)
        return custom_images


    def link(self, user_id, character_id, image_id):
        raise NotImplementedError()

    def unlink(self, user_id, character_id, image_id):
        raise NotImplementedError()