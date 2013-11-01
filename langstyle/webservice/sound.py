
import shutil
from . import util
from . import web
from . import sound_for_test

class SoundHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self._character = None

    def get(self):
        self._character = self._get_character()
        if sound_for_test.exists(self._character):
            self._send_headers()
            sound_stream = sound_for_test.get(self._character)
            shutil.copyfileobj(sound_stream, self._request.wfile)
            sound_stream.close()
        else:
            self.send_error(404)

    def _get_character(self):
        return util.get_path_tail(self.get_path())

    def get_content_type(self):
        return sound_for_test.get_content_type(self._character)

    def get_content_length(self):
        return sound_for_test.get_sound_size(self._character)

    def _send_headers(self):
        self.set_response_code(200)
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", self.get_content_length())
        self.send_headers()