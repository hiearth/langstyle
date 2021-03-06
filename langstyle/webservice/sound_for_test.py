
# download sound from http://www.howjsay.com/mp3/$word$.mp3

import os
from . import util
from .. import config

SOUND_EXTENSION = ".mp3"

def _get_full_path(character):
    return os.path.abspath(os.path.join(config.DATA_DIRECTORY, "sound", character + SOUND_EXTENSION))

def exists(character):
    sound_path = _get_full_path(character)
    return os.path.exists(sound_path)

def get(character):
    sound_path = _get_full_path(character)
    return open(sound_path, "rb")

def get_content_type(character):
    sound_path = _get_full_path(character)
    sound_suffix = util.get_file_suffix(sound_path)
    return util.HttpUtil.get_content_type(sound_suffix)

def get_sound_size(character):
    sound_path = _get_full_path(character)
    return util.get_file_size(sound_path)
