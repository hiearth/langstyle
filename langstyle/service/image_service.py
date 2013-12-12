#!/usr/bin/env python

class ImageService:
    '''image service for public'''

    def __init__(self, image_repository):
        self._image_repository = image_repository

    def get(self, image_id):
        # 1. get image path from image repository
        # 2. read image data from file service
        return self._image_repository.get(image_id)

    def add(self, image_data):
        # 1. file service to save the image data in the file system
        # 2. image repository store summary image info, such as id, imagePath, providerUserId, md5(maybe) and so on
        # 3. if image repository add action fail, file service can rollback to delete the saved image file
        return self._image_repository.add(image_data)