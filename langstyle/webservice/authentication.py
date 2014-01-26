#!/usr/bin/env python

from . import web
from .. import config

class AuthenticationHandler(web.RequestHandler):

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
        if not user_service.authenticate(user_name, password):
            self.send_server_error("user name or password is wrong")
            return
        self.set_cookie("userName", user_name)
        self.send_success_headers()