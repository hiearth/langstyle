#!/usr/bin/env python

from . import base_repository
from .. import helper

class CharacterImageRepository(base_repository.BaseRepository):

    def get_images(self, user_id, character_id):
        custom_images = self._call_proc_query_all(
            "CharacterImage_Images_S", [user_id, character_id])
        return helper.list_comprehension_by_index(custom_images, 0)

    def get_most_used_images(self, character_id, image_count):
        statistic_images = self._call_proc_query_all(
            "CharacterImage_Statistic_S", [character_id, image_count])
        return helper.list_comprehension_by_index(statistic_images, 0)

    def link(self, user_id, character_id, image_id):
        self._call_proc_non_query("CharacterImage_I", [user_id, character_id, image_id])

    def unlink(self, user_id,character_id, image_id):
        self._call_proc_non_query("CharacterImage_D", [user_id,character_id, image_id])