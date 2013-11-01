
import os
import shutil
from . import util

class RequestHandler:

    def __init__(self, request):
        self._request = request
        self._headers = {}

    def get(self):
        raise NotImplementedError()

    def post(self):
        raise NotImplementedError()

    def put(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def head(self):
        raise NotImplementedError()
    
    def get_path(self):
        return self._request.path

    def get_content_type(self):
        pass

    def get_content_length(self):
        pass

    def set_response_code(self, code, message=None):
        self._request.send_response(code, message)

    def set_header(self, key, value):
        self._headers[key] = value

    def send_headers(self):
        for key, value in self._headers.items():
            self._request.send_header(key, value)
        self._request.end_headers()

    def send_content(self, str):
        content_bytes = str.encode(encoding = "utf-8")
        self._request.wfile.write(content_bytes)

    def send_error(self, status_code, message=None):
        self._request.send_error(status_code, message)


class StaticFileHandler(RequestHandler):
    
    def __init__(self, request):
        super().__init__(request)
        self._file_path = ""

    def get(self):
        self._file_path = self.get_full_path()
        if os.path.exists(self._file_path):
            self._send_headers()
            self.send_content()
        else:
            self.send_error(404)

    def get_content_type(self):
        file_suffix = util.get_file_suffix(self._file_path)
        return util.HttpUtil.get_content_type(file_suffix)

    def get_content_length(self):
        return util.get_file_size(self._file_path)

    def _send_headers(self):
        self.set_response_code(200)
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", self.get_content_length())
        self.send_headers()

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