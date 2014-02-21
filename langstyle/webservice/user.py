#!/usr/bin/env python

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
        self.set_cookie("userName", user_name, 2592000)
        self.send_headers_and_content(str(user_id))