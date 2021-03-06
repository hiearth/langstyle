#!/usr/bin/env python

import os
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from .webservice import router
from . import config

class HTTPRequestHandler(BaseHTTPRequestHandler):
    """handle all types of request"""

    def _get_handler(self):
        request_handler_router = router.RequestHandlerRouter()
        handler_class = request_handler_router.get_handler(self)
        if handler_class:
            return handler_class(self)
        return None

    def _call_handle_method(self, handle_method):
        try:
            handler = self._get_handler()
            if handler:
                request_handle = getattr(handler, handle_method)
                if request_handle:
                    request_handle()
        except Exception as e:
            config.service_factory.get_log_service().error(str(e))
            self.send_error(500)

    def do_GET(self):
        self._call_handle_method("get")

    def do_POST(self):
        self._call_handle_method("post")

    def do_PUT(self):
        self._call_handle_method("put")

    def do_DELETE(self):
        self._call_handle_method("delete")

    def do_HEAD(self):
        self._call_handle_method("head")

def start():
    port = os.getenv("OPENSHIFT_PYTHON_PORT", default=8000)
    port = int(port)
    serverAddress = os.getenv("OPENSHIFT_PYTHON_IP", default="127.0.0.1")
    BaseHTTPRequestHandler.protocol_version = "HTTP/1.0"
    server = HTTPServer((serverAddress, port), HTTPRequestHandler)
    print("server start, address: " + serverAddress + ":" + str(port))
    server.serve_forever()
