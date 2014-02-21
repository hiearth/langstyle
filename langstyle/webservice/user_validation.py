#!/usr/bin/env python

from . import web
from .. import config

class UserValidationHandler(web.RequestHandler):

    def get(self):
        user_name = self.get_query_parameter("userName")
        if user_name:
            user_service = config.service_factory.get_user_service()
            if user_service.exist(user_name):
                self.send_bad_request("user name already exist")
                return
        self.send_success_headers()