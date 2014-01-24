#!/usr/bin/env python

from . import web
from .. import config

class UserHandler(web.RequestHandler):

    def get(self):
        pass

    def post(self):
        userName = self.get_form_parameter("userName")
        if not userName:
            self.send_bad_request("user name is required")
            return
        password = self.get_form_parameter("password")
        if not password:
            self.send_bad_request("password is required")
            return
        user_service = config.service_factory.get_user_service()
        user_id = user_service.add(userName, password, None)
        if user_id is None:
            self.send_server_error("fail to register user")
            return
        self.send_headers_and_content(str(user_id))