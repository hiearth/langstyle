#!/usr/bin/env python

from .. import config

class ImageService:
    '''image service for public'''

    def __init__(self, image_repository):
        self._image_repository = image_repository
        self._image_file_service = config.service_factory.get_image_file_service()

    def get(self, image_id):
        image_item = self._image_repository.get(image_id)
        if image_item:
            return self._image_file_service.read(image_item.path)
        return None

    def add(self, image_data):
        # 1. file service to save the image data in the file system
        # 2. image repository store summary image info, such as id, imagePath, providerUserId, md5(maybe) and so on
        # 3. if image repository add action fail, file service can rollback to delete the saved image file
        return self._image_repository.add(image_data)