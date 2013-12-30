#!/usr/bin/env python

from .. import config
from .. import helper

class ImageService:
    '''image service for public'''

    def __init__(self, image_repository, image_file_service):
        self._image_repository = image_repository
        self._image_file_service = image_file_service

    def get(self, image_id):
        image_item = self._image_repository.get(image_id)
        if image_item:
            return self._image_file_service.read(image_item.md5)
        return None

    def get_key(self, image_id):
        image_item = self._image_repository.get(image_id)
        if image_item:
            return image_item.md5
        return None

    def add(self, image_data, user_provider_id):
        # 1. file service to save the image data in the file system
        # 2. image repository store summary image info, such as id, providerUserId, md5 and so on
        # 3. if image repository add action fail, file service can rollback to delete the saved image file
        image_md5 = helper.md5_hash(image_data)
        try:
            self._image_file_service.write(image_md5, image_data)
            image_id = self._image_repository.add(image_md5, user_provider_id)
            return image_id
        except Exception as e:
            config.service_factory.get_log_service().error(e.args[0])
        return None
