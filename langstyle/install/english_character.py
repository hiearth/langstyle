#!/usr/bin/env python

import os
from .. import config

cet4_file = os.path.join(config.DATA_DIRECTORY, "CET4_all.txt")
cet6_file = os.path.join(config.DATA_DIRECTORY, "CET6_more_frequent.txt")
cet_file = os.path.join(config.DATA_DIRECTORY, "CET.txt")

def populate_cet_characters():
    cet_characters = _get_cet_characters()
    character_service = config.service_factory.get_character_service()
    for c in cet_characters:
        character_service.add(c)

def _get_cet_characters():
    if not os.path.exists(cet_file):
        _format()
    return _get_characters_from_file(cet_file)

def _format():
    cet4_characters = _get_characters_from_file(cet4_file)
    cet6_characters = _get_characters_from_file(cet6_file)
    characters = []
    _add_characters(characters, cet4_characters)
    _add_characters(characters, cet6_characters)
    characters.sort()
    _write_characters_to_file(characters)

def _get_characters_from_file(file_path):
    characters = []
    with(open(file_path, mode="r", encoding="utf-8")) as f:
        lines = f.readlines()
    if lines:
        for line in lines:
            characters.extend(_get_character_list_in_line(line))
    return characters

def _add_characters(characters, new_characters):
    for c in new_characters:
        if c not in characters:
            characters.append(c)

def _get_character_list_in_line(line):
    if line:
        characters = line.split()
        return characters
    return []

def _write_characters_to_file(characters):
    if characters:
        with open(cet_file, mode="a", encoding="utf-8") as f:
            for c in characters:
                f.write(c + os.linesep)