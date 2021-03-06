
import re
from .. import helper
from . import web
from . import user
from . import authentication
from . import page
from . import image
from . import sound
from . import character
from . import character_image
from . import character_sound
from . import user_validation
from . import user_progress

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
        self._add_handler(r"/([a-zA-Z]*)(\.html)$", page.HTMLHandler)
        self._add_handler(r"/user/(.*)", user.UserHandler)
        self._add_handler(r"/user$", user.UserHandler)
        self._add_handler(r"/uservalidation\?(.*)", user_validation.UserValidationHandler)
        self._add_handler(r"/authentication/?(.*)", authentication.AuthenticationHandler)
        self._add_handler(r"/character/(.*)", character.CharacterHandler)
        self._add_handler(r"/charactercode/?(.*)", character.CharacterCodeHandler)
        self._add_handler(r"/image/?(.*)", image.ImageHandler)
        self._add_handler(r"/characterimages/(.*)", character_image.CharacterImagesHandler)
        self._add_handler(r"/characterimage/character/([0-9a-zA-Z]*)/image/(.*)", character_image.CharacterImageHandler)
        self._add_handler(r"/charactersounds/(.*)", character_sound.CharacterSoundsHandler)
        self._add_handler(r"/charactersound/character/([0-9a-zA-Z]*)/sound/(.*)", character_sound.CharacterSoundHandler)
        self._add_handler(r"/sound/?(.*)",sound.SoundHandler)
        self._add_handler(r"/userprogress/next", user_progress.UserProgressNextHandler)
        self._add_handler(r"/charactertest", user_progress.CharacterTestHandler)
        self._add_handler(r"(.*)\.js", web.StaticFileHandler)
        self._add_handler(r"(.*)\.css", web.StaticFileHandler)
        self._add_handler(r"(.*)\.png", web.StaticFileHandler)
        self._add_handler(r"(.*)\.html", web.StaticFileHandler)

    def _add_handler(self, pattern, handler_class):
        self._routes.append((re.compile(pattern), handler_class))

    def get_handler(self, request):
        """return a matched handler class"""
        for pattern, handler_class in self._routes:
            if pattern.match(request.path):
                return handler_class
        return web.NotFoundHandler

    def get_regex(self, handler_class):
        handler_filter = (lambda route: route[1] == handler_class)
        route = helper.find_first(self._routes, handler_filter)
        if route:
            return route[0]
        return None
