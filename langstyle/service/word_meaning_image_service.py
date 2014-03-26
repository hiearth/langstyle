#!/usr/bin/env python

from .. import config
from .. import helper

class WordMeaningImageService:

    def __init__(self, word_meaning_image_repository):
        self._word_meaning_image_repository = word_meaning_image_repository

    def _need_additional_images(self, custom_images):
        return len(custom_images) < config.IMAGES_COUNT_PER_WORD_MEANING

    def _combine_custom_and_statistic(self, custom_images, statistic_images):
        image_not_custom = (lambda image_id: image_id not in custom_images)
        additional_count = config.IMAGES_COUNT_PER_WORD_MEANING - len(custom_images)
        return helper.chain_lists(custom_images, helper.get_matched_items(
            statistic_images, image_not_custom, additional_count))

    def get_images(self, user_id, word_meaning_id):
        custom_images = self._word_meaning_image_repository.get_images(user_id, word_meaning_id)
        if self._need_additional_images(custom_images):
            statistic_images = self._word_meaning_image_repository.get_most_used_images(
                word_meaning_id, config.IMAGES_COUNT_PER_WORD_MEANING)
            return self._combine_custom_and_statistic(custom_images, statistic_images)
        return custom_images

    def link_exist(self, user_id, word_meaning_id, image_id):
        custom_images = self._word_meaning_image_repository.get_images(
            user_id, word_meaning_id)
        return image_id in custom_images

    def link(self, user_id, word_meaning_id, image_id):
        if not self.link_exist(user_id, word_meaning_id, image_id):
            self._word_meaning_image_repository.link(user_id, word_meaning_id, image_id)

    def unlink(self, user_id, word_meaning_id, image_id):
        self._word_meaning_image_repository.unlink(user_id, word_meaning_id, image_id)
