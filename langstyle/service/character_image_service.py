#!/usr/bin/env python

from .. import config
from .. import helper

class CharacterImageService:

    def __init__(self, character_image_repository):
        self._character_image_repository = character_image_repository

    def _need_additional_images(self, custom_images):
        return len(custom_images) < config.IMAGES_COUNT_PER_CHARACTER

    def _combine_custom_and_statistic(self, custom_images, statistic_images):
        image_not_custom = (lambda image_id: image_id not in custom_images)
        additional_count = config.IMAGES_COUNT_PER_CHARACTER - len(custom_images)
        return helper.chain_lists(custom_images, helper.get_matched_items(
            statistic_images, image_not_custom, additional_count))

    def get_images(self, user_id, character_id):
        custom_images = self._character_image_repository.get_images(user_id, character_id)
        if self._need_additional_images(custom_images):
            statistic_images = self._character_image_repository.get_most_used_images(
                character_id, config.IMAGES_COUNT_PER_CHARACTER)
            return self._combine_custom_and_statistic(custom_images, statistic_images)
        return custom_images

    def link_exist(self, user_id, character_id, image_id):
        custom_images = self._character_image_repository.get_images(
            user_id, character_id)
        return image_id in custom_images

    def link(self, user_id, character_id, image_id):
        if not self.link_exist(user_id, character_id, image_id):
            self._character_image_repository.link(user_id, character_id, image_id)

    def unlink(self, user_id, character_id, image_id):
        self._character_image_repository.unlink(user_id, character_id, image_id)