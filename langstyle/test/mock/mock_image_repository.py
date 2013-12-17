#!/usr/bin/env python

from langstyle import helper
from langstyle.database import image_repository

class MockImageRepository:

    def __init__(self):
        self._images = []

    def get(self, image_id):
        find_by_id = (lambda image_item: image_item.id == image_id)
        return helper.find_first(self._images, find_by_id)

    def add(self, image_md5, user_provider_id):
        image_item = image_repository.WordImage(md5=image_md5)
        self._images.append(image_item)
        image_item.id = len(self._images)
        return image_item.id
