#!/usr/bin/env python

import os
import re
import time
from socket import timeout
import urllib.request
from .. import config

character_dir = os.path.join(config.ENGLISH_POPULATION_DIRECTORY, "character")
sound_dir = os.path.join(config.ENGLISH_POPULATION_DIRECTORY, "sound")
cet4_file = os.path.join(character_dir, "CET4_all.txt")
cet6_file = os.path.join(character_dir, "CET6_more_frequent.txt")
cet_file = os.path.join(character_dir, "CET.txt")

sound_download_urls = [("http://translate.google.com.hk/translate_tts?ie=UTF-8&tl=en&q=","uk"),
                       ("http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=","us")]

# sound
def populate_sounds():
    characters = _get_cet_characters()
    for c in characters:
        _link_character_and_sound(c)

def _link_character_and_sound(character_code):
    character_id = config.service_factory.get_character_service().get_id(character_code)
    for url, country in sound_download_urls:
        sound_data = _get_sound(character_code, country)
        sound_id = config.service_factory.get_sound_service().add(sound_data, config.ADMINISTRATOR_ID)
        config.service_factory.get_character_sound_service().link(config.ADMINISTRATOR_ID, character_id, sound_id)

def _get_sound(character_code, country):
    if not _sound_exist(character_code, country):
        _retrive_sound_and_save(character_code)
    sound_file_path = _get_sound_file_path(character_code, country)
    return _read_file(sound_file_path)

def _read_file(file_path):
    with open(file_path, "rb") as f:
        return f.read()

def _retrive_sounds():
    characters = _get_cet_characters()
    for c in characters:
        _retrive_sound_and_save(c)

def _retrive_sound_and_save(character_code):
    for download_url, country in sound_download_urls:
        if not _sound_exist(character_code, country):
            _download_and_save(character_code, download_url + character_code, country)
            time.sleep(2)

def _sound_exist(character_code, country):
    return os.path.exists(_get_sound_file_path(character_code, country))

def _get_sound_file_path(character_code, country):
    return os.path.join(sound_dir, "".join((character_code, "_", country)))

def _download_and_save(character_code, sound_url, country):
    try:
        sound_data = _download(sound_url)
        sound_file_path = _get_sound_file_path(character_code, country)
        _save_to_file(sound_file_path, sound_data)
    except Exception as e:
        config.service_factory.get_log_service().error("Fail to save sound of character:" + character_code)

def _download(sound_url):
    try:
        config.service_factory.get_log_service().debug("requesting " + sound_url)
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0"
        headers = {"User-Agent": user_agent}
        url_request = urllib.request.Request(sound_url, headers=headers)
        response = urllib.request.urlopen(url_request, timeout=30)
        sound_data = response.read()
        return sound_data
    except Exception as e:
        error_msg = " ".join(["Error when accessing",sound_url,str(e)])
        config.service_factory.get_log_service().error(error_msg)
    except timeout:
        config.service_factory.get_log_service().error("time out")
    return None

def _save_to_file(file_path, content):
    with open(file_path, "wb") as f:
        f.write(content)


# character
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
    return line.split() if line else []

def _write_characters_to_file(characters):
    if characters:
        with open(cet_file, mode="a", encoding="utf-8") as f:
            for c in characters:
                f.write(c + os.linesep)


# words

dictionary_dir = os.path.join(config.ENGLISH_POPULATION_DIRECTORY, "dictionary")
word_level_1_file = os.path.join(dictionary_dir, "level_1.txt")
word_level_2_file = os.path.join(dictionary_dir, "level_2.txt")
word_level_3_file = os.path.join(dictionary_dir, "level_3.txt")
word_level_4_file = os.path.join(dictionary_dir, "level_4.txt")

def chinese_english_words():
    language_map_service = config.service_factory.get_language_map_service()
    chinese_to_english_map_id = language_map_service.get_id("Chinese", "English")
    level_files = [(word_level_1_file, 1),(word_level_2_file, 2),
                   (word_level_3_file, 3),(word_level_4_file, 4)]
    character_service = config.service_factory.get_character_service()
    word_meaning_service = config.service_factory.get_word_meaning_service()
    for file_name, level in level_files:
        word_meanings = _get_words_in_file(file_name)
        for character_code, explaination in word_meanings:
            character_id = character_service.add(character_code)
            word_meaning_service.add(character_id,chinese_to_english_map_id, explaination, level)

def _get_words_in_file(file_name):
    with(open(file_name, mode="r", encoding="utf-8")) as f:
        lines = f.readlines()
    return _get_word_meanings(lines)

def _get_word_meanings(lines):
    if not lines:
        return []
    return [_get_word_meaning_in_line(line) for line in lines 
            if _has_word_meaning_in_line(line)]

def _has_word_meaning_in_line(line):
    if line:
        return (len(line.strip()) > 0) and (len(line.split()) == 2)
    return False

def _get_word_meaning_in_line(line):
    return line.split() if line else None


# image
image_dir = os.path.join(config.ENGLISH_POPULATION_DIRECTORY, "image")
image_level_1_dir = os.path.join(image_dir, "level_1")
image_file_regex = re.compile(r"(.*)_([0-9]+)\.jpg")

def populate_images():
    language_map_service = config.service_factory.get_language_map_service()
    chinese_to_english_map_id = language_map_service.get_id("Chinese", "English")
    level_dirs = [(image_level_1_dir, 1)]
    for level_dir, level in level_dirs:
        _link_words_in_level(level_dir, level, chinese_to_english_map_id)

def _link_words_in_level(level_dir, level, language_map_id):
    word_meanings = config.service_factory.get_word_meaning_service().get_by_level(language_map_id,level)
    for word_item in word_meanings:
        related_images = _get_images_by_character(os.listdir(level_dir),word_item.character_code)
        image_paths = [os.path.join(level_dir, image_file_name) 
                       for image_file_name in related_images]
        _link_image_and_word(image_paths, word_item.id)

def _link_image_and_word(image_paths,word_meaning_id):
    for image_path in image_paths:
        image_data = _read_file(image_path)
        image_id = config.service_factory.get_image_service().add(image_data,config.ADMINISTRATOR_ID)
        config.service_factory.get_word_meaning_image_service().link(config.ADMINISTRATOR_ID, word_meaning_id, image_id)

def _get_images_by_character(file_names,character_code):
    image_files = []
    for file_name in file_names:
        file_pattern = image_file_regex.findall(file_name)
        if file_pattern and file_pattern[0][0]==character_code:
            image_files.append(file_name)
    return image_files


