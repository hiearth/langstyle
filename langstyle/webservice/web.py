
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
        self._request_body = {}
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

    def get(self):
        '''get'''
        raise NotImplementedError()

    def post(self):
        '''add'''
        raise NotImplementedError()

    def put(self):
        '''update'''
        raise NotImplementedError()

    def delete(self):
        '''delete'''
        raise NotImplementedError()

    def head(self):
        '''get header'''
        raise NotImplementedError()    
    def has_permission(self):
        return self.user_id is not None

    def get_body(self):
        body_length = self._request.headers.get("content-length")
        post_vars = urllib.parse.parse_qs(self._request.rfile.read(int(body_length)), keep_blank_values=1)
        return post_vars

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

    def get_content_length(self):
        return 0

    def set_response_code(self, code, message=None):
        self._request.send_response(code, message)

    def set_header(self, key, value):
        self._response_headers[key] = value

    def send_headers(self):
        for key, value in self._response_headers.items():
            self._request.send_header(key, value)
        self._request.end_headers()

    def send_content(self, str):
        if str is None:
            str = "Not Found"
        content_bytes = str.encode(encoding = "utf-8")
        self._request.wfile.write(content_bytes)

    def send_success_headers(self):
        self.set_response_code(200)
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", self.get_content_length())
        self.send_headers()

    def send_not_found(self):
        self.send_error(404)

    def send_access_denied(self):
        self.send_error(401, "No permission")

    def send_error(self, status_code, message=None):
        self._request.send_error(status_code, message)

    def _log_error(self, msg):
        config.service_factory.get_log_service().error(msg)


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
            self.send_error(404)

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