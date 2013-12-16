#!/usr/bin/env python

from langstyle import helper

class MockImageRepository:

    def __init__(self):
        self._images = []

    def add(self, image_data):
        pass

    def get(self, image_id):
        find_by_id = (lambda image_item: image_item.id == image_id)
        return helper.find_first(self._images, find_by_id)


class WordImage:

    def __init__(self):
        #self._id = None
        self._path = None

    #@property
    #def id(self):
    #    return self._id

    #@id.setter
    #def id(self, value):
    #    self._id = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value