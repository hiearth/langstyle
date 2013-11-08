
import os
from . import util

#ROOT_DIRECTORY = os.path.join("langstyle", "image")
ROOT_DIRECTORY = os.path.join("data", "image")
IMAGE_EXTENSION = ".jpg"


def _get_full_path(character):
    return os.path.abspath(os.path.join(ROOT_DIRECTORY,character + IMAGE_EXTENSION))

def exists(character):
    image_path = _get_full_path(character)
    return os.path.exists(image_path)

def get(character):
    image_path = _get_full_path(character)
    return open(image_path, "rb")

def add(character, newImage):
    pass

def update(character, updateImage):
    pass

def get_content_type(character):
    image_path = _get_full_path(character)
    image_suffix = util.get_file_suffix(image_path)
    return util.HttpUtil.get_content_type(image_suffix)

def get_image_size(character):
    image_path = _get_full_path(character)
    return util.get_file_size(image_path)
