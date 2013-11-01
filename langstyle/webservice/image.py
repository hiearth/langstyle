
import shutil
from . import util
from . import web
from . import image_for_test

class ImageHandler(web.RequestHandler):

    def __init__(self, request):
        super().__init__(request)
        self._character = None

    def get(self):
        self._character = self._get_character()
        if image_for_test.exists(self._character):
            self._send_headers()
            image_stream = image_for_test.get(self._character)
            shutil.copyfileobj(image_stream, self._request.wfile)
            image_stream.close()
        else:
            self.send_error(404)

    #def post(self):
    #    # get word by character
    #    # call image_for_test.add
    #    pass

    #def put(self):
    #    # get word by character
    #    # call image_for_test.update
        #pass

    def _get_character(self):
        return util.get_path_tail(self.get_path())

    def get_content_type(self):
        return image_for_test.get_content_type(self._character)

    def get_content_length(self):
        return image_for_test.get_image_size(self._character)

    def _send_headers(self):
        self.set_response_code(200)
        self.set_header("Content-Type", self.get_content_type())
        self.set_header("Content-Length", self.get_content_length())
        self.send_headers()