#!/usr/bin/env python

from . import base_repository
from .. import helper

class WordMeaningImageRepository(base_repository.BaseRepository):

    def get_images(self, user_id, word_meaning_id):
        custom_images = self._call_proc_query_all(
            "WordMeaningImage_Images_S", [user_id, word_meaning_id])
        return helper.list_comprehension_by_index(custom_images, 0)

    def get_most_used_images(self, word_meaning_id, image_count):
        statistic_images = self._call_proc_query_all(
            "WordMeaningImage_Statistic_S", [word_meaning_id, image_count])
        return helper.list_comprehension_by_index(statistic_images, 0)

    def link(self, user_id, word_meaning_id, image_id):
        self._call_proc_non_query("WordMeaningImage_I", [user_id, word_meaning_id, image_id])

    def unlink(self, user_id, word_meaning_id, image_id):
        self._call_proc_non_query("WordMeaningImage_D", [user_id, word_meaning_id, image_id])
