
from . import web

class HTMLHandler(web.StaticFileHandler):

    def resolve_path_to_local_path(self):
        request_path = self.get_path()
        if request_path == "/" or request_path == "":
            return "index.html"
        return super().resolve_path_to_local_path()