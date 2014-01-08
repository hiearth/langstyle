
import os
import shutil
import http
import http.cookies
import urllib.parse
from . import util
from .. import config

class RequestHandler:

    def __init__(self, request):
        self._request = request
        self._response_headers = {}
        self._request_form = None
        self.user_id = self._get_user()

    def _get_user(self):
        user_value = self.get_cookie("user")
        if user_value is not None:
            try:
                return int(user_value)
            except ValueError as e:
                self._log_error(str(e))
        # to do need return None
        return 1

    def _get_regex(self):
        from . import router
        request_handler_router = router.RequestHandlerRouter()
        return request_handler_router.get_regex(type(self))

    def get(self):
        '''get'''
        self.send_method_not_allowed()

    def post(self):
        '''add'''
        self.send_method_not_allowed()

    def put(self):
        '''update'''
        self.send_method_not_allowed()

    def delete(self):
        '''delete'''
        self.send_method_not_allowed()

    def head(self):
        '''get header'''
        self.send_method_not_allowed()    
    def has_permission(self):
        return self.user_id is not None

    def get_form_parameter(self, parameter_name):
        form = self.get_request_form()
        parameter_value = form.get(parameter_name.encode(), None)
        if parameter_value:
            return parameter_value[0].decode()
        return None

    def get_request_form(self):
        if self._request_form is None:
            body_length = self._request.headers.get("content-length")
            self._request_form = urllib.parse.parse_qs(self._request.rfile.read(int(body_length)), keep_blank_values=1)
        return self._request_form

    def get_file(self):
        body_length = self._request.headers.get("content-length")
        return self._request.rfile.read(int(body_length))

    def get_cookie(self, cookie_name):
        request_cookie = self._request.headers.get("cookie")
        cookie = http.cookies.SimpleCookie()
        if request_cookie:
            cookie.load(request_cookie)
            cookie_item = cookie.get(cookie_name, None)
            if cookie_item:
                return cookie_item.value
        return None
    
    def get_path(self):
        return self._request.path

    def get_content_type(self):
        return "text/plain"

    def set_response_code(self, code, message=None):
        self._request.send_response(code, message)

    def set_header(self, key, value):
        self._response_headers[key] = value

    def _send_headers(self):
        for key, value in self._response_headers.items():
            self._request.send_header(key, value)
        self._request.end_headers()

    def send_success_headers(self):
        self.set_response_code(200)
        self.set_header("Connection", "close")
        self._send_headers()

    def send_headers_and_content(self, content):
        self.set_response_code(200)
        content = self._convert_content_to_bytes(content)
        self._set_content_headers(content)
        self._send_headers()
        self._write_response_content(content)

    def _set_content_headers(self, content):
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", len(content))

    def _convert_content_to_bytes(self, content):
        if content is None:
            return b""
        if type(content) is str:
            return content.encode(encoding="utf-8")
        return content

    def _write_response_content(self, content_bytes):
        self._request.wfile.write(content_bytes)

    def send_not_found(self):
        self._send_error(404, "Not Found")

    def send_access_denied(self):
        self._send_error(401, "No permission")

    def send_method_not_allowed(self):
        self._send_error(405, "Method Not Allowed")

    def _send_error(self, status_code, message="Error"):
        self.set_response_code(status_code, message)
        message = self._convert_content_to_bytes(message)
        self._set_content_headers(message)
        self.set_header("Connection", "close")
        self._send_headers()
        self._write_response_content(message)

    def _log_error(self, msg):
        config.service_factory.get_log_service().error(msg)


class NotFoundHandler(RequestHandler):

    def get(self):
        self.send_not_found()


class StaticFileHandler(RequestHandler):
    
    def __init__(self, request):
        super().__init__(request)
        self._file_path = ""

    def get(self):
        self._file_path = self.get_full_path()
        if os.path.exists(self._file_path):
            self.send_success_headers()
            self.send_content()
        else:
            self.send_not_found()

    def get_content_type(self):
        file_suffix = util.get_file_suffix(self._file_path)
        return util.HttpUtil.get_content_type(file_suffix)

    def get_content_length(self):
        return util.get_file_size(self._file_path)

    def send_content(self):
        with open(self._file_path, self._get_read_mode()) as f:
            shutil.copyfileobj(f, self._request.wfile)

    def _get_read_mode(self):
        return "rb"

    def resolve_path_to_local_path(self):
        request_path = os.path.normpath(self.get_path())
        if request_path.startswith(os.sep):
            return request_path.replace(os.sep, "",1)
        return request_path
    
    def get_full_path(self):
        root_directory = self.get_root_directory()
        request_path = self.resolve_path_to_local_path()
        return os.path.abspath(os.path.join(root_directory, request_path))

    def get_root_directory(self):
        return os.path.join("langstyle","ui")