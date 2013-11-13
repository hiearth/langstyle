
import os
from . import util

ROOT_DIRECTORY = os.path.abspath(os.path.join("data", "image"))
SUFFIX = "txt"

def _get_all_characters():
    characters = []
    for root_path, dirs, files in os.walk(ROOT_DIRECTORY):
        characters = [_get_character_from_file_name(f) for f in files if _is_character_file(f)]
    return characters

def _get_character_from_file_name(file_name):
    return util.get_file_name(file_name)

def _is_character_file(file_name):
    return util.get_file_suffix(file_name) == "jpg"

def exists(character):
    return character in _get_all_characters()

def get(character):
    if not exists(character):
        character = None
    characters = _get_all_characters()
    if character:
        character_index = characters.index(character)
        if character_index != len(characters) - 1:
            return characters[character_index + 1]
    return characters[0]

def get_content_type():
    return util.HttpUtil.get_content_type(SUFFIX)
