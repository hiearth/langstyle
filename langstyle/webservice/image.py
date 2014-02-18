#!/usr/bin/env python

import shutil
from . import util
from . import web
from .. import config

class ImageHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self._character = None

    def _get_service(self):
        return config.service_factory.get_image_service()

    def get(self):
        image_id = self._get_request_image()
        image_content = self._get_service().get(image_id)
        if image_content is None:
            self.send_not_found()
            return
        self.send_headers_and_content(image_content)

    def _get_request_image(self):
        image_ids = self._get_regex().findall(self.get_path())
        if image_ids:
            return image_ids[0]
        return None

    def get_content_type(self):
        return "image/jpeg"

    def post(self):
        image_file = self.get_file()
        imageId = self._get_service().add(image_file, self.user_id)
        self.send_headers_and_content(str(imageId))