
import re
from . import web
from . import page
from . import image
from . import sound
from . import character
from . import user_character

# meta class
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class RequestHandlerRouter(metaclass=Singleton):
    """route request to corresponding handler"""

    def __init__(self):
        self._routes = []
        self._add_handler(r"/$", page.HTMLHandler)
        self._add_handler(r"/character/(.*)", character.CharacterHandler)
        self._add_handler(r"/usercharacter/grasp", user_character.UserCharacterGraspHandler)
        self._add_handler(r"/usercharacter/current", user_character.UserCharacterCurrentHandler)
        self._add_handler(r"/image/(.*)", image.ImageHandler)
        self._add_handler(r"/sound/(.*)",sound.SoundHandler)
        self._add_handler(r"(.*)\.js", web.StaticFileHandler)
        self._add_handler(r"(.*)\.css", web.StaticFileHandler)

    def _add_handler(self, pattern, handler_class):
        self._routes.append((re.compile(pattern), handler_class))

    def get_handler(self, request):
        """return a matched handler class"""
        for pattern, handler_class in self._routes:
            if pattern.match(request.path):
                return handler_class
        return None
