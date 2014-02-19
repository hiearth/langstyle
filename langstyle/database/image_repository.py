#!/usr/bin/env python

from . import base_repository
from ..entity import word_image

class ImageRepository(base_repository.BaseRepository):

    def get(self, image_id):
        image_result = self._call_proc_query_one(
            "WordImage_S_By_Id", [image_id])
        if image_result:
            return word_image.WordImage(
                image_id, image_result[0], image_result[1])
        return None

    def add(self, image_md5, user_provider_id):
        result = self._call_proc_non_query(
            "WordImage_I", [image_md5, user_provider_id, None])
        if result:
            return result[2]
        return None