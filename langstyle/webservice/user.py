#!/usr/bin/env python

#import pdb
from . import web
from .. import config

class UserHandler(web.RequestHandler):

    def get(self):
        pass

    def post(self):
        user_name = self.get_form_parameter("userName")
        if not user_name:
            self.send_bad_request("user name is required")
            return
        password = self.get_form_parameter("password")
        if not password:
            self.send_bad_request("password is required")
            return
        user_service = config.service_factory.get_user_service()
        if user_service.exist(user_name):
            self.send_bad_request("user name already exist")
            return
        user_id = user_service.add(user_name, password, None)
        if user_id is None:
            self.send_server_error("fail to register user")
            return
        self._set_language_map(user_id)
        self.set_cookie("userName", user_name, 2592000)
        self.set_cookie("userId", user_id, 2592000, True)
        self.send_headers_and_content(str(user_id))

    def _set_language_map(self, user_id):
        user_info = config.service_factory.get_user_service().get_by_id(user_id)
        if user_info.language_map_id is None:
            language_map_service = config.service_factory.get_language_map_service()
            chinese_to_english_id = language_map_service.get_id("Chinese", "English")
            config.service_factory.get_user_service().update_language_map(user_id,chinese_to_english_id)

