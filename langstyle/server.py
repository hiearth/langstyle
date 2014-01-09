#!/usr/bin/env python

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from .webservice import router

class HTTPRequestHandler(BaseHTTPRequestHandler):
    """handle all types of request"""

    def _get_handler(self):
        request_handler_router = router.RequestHandlerRouter()
        handler_class = request_handler_router.get_handler(self)
        if handler_class:
            return handler_class(self)
        return None

    def _call_handle_method(self, handle_method):
        handler = self._get_handler()
        if handler:
            request_handle = getattr(handler, handle_method)
            if request_handle:
                request_handle()

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
    protocol = "HTTP/1.0"
    port = 8000
    serverAddress = "0.0.0.0"
    BaseHTTPRequestHandler.protocol_version = protocol
    server = HTTPServer((serverAddress, port), HTTPRequestHandler)
    print("server start, address: " + serverAddress + ":" + str(port))
    server.serve_forever()