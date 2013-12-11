#!/usr/bin/env python

class ImageService:
    '''image service for public'''

    def __init__(self, image_repository):
        self._image_repository = image_repository

    def get(self, image_id):
        pass