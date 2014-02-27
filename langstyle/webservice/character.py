#!/usr/bin/env python

import urllib.request
import concurrent.futures
import time
from . import util
from . import web
from .. import config

class CharacterHandler(web.RequestHandler):

    def _get_service(self):
        return config.service_factory.get_character_service()

    def get(self):
        character_id = self._get_request_character()
        if character_id is None:
            self.send_not_found()
            return
        character_service = self._get_service()
        character_code = character_service.get(character_id)
        if character_code is None:
            self.send_not_found()
            return
        self.send_headers_and_content(character_code)

    def _get_request_character(self):
        characters = self._get_regex().findall(self.get_path())
        if characters:
            try:
                return int(characters[0])
            except ValueError as e:
                self._log_error(str(e))
        return None


class CharacterCodeHandler(web.RequestHandler):

    def _get_service(self):
        return config.service_factory.get_character_service()

    def get(self):
        character_code = self._get_request_character_code()
        character_id = self._get_service().get_id(character_code)
        if character_id is None:
            self.send_not_found()
            return
        self.send_headers_and_content(str(character_id))

    def post(self):
        character_code = self._get_request_character_code()
        if not self._get_service().exist(character_code):
            character_id = self._add(character_code)
        else:
            character_id = self._get_service().get_id(character_code)
        if character_id is None:
            self.send_server_error("Fail to add character.")
            return
        self.send_headers_and_content(str(character_id))

    def _add(self, character_code):
        character_id = self._get_service().add(character_code)
        if character_id is not None:
            download_sound(character_code, character_id, self.user_id)
        return character_id

    def _get_request_character_code(self):
        character_codes = self._get_regex().findall(self.get_path())
        if character_codes:
            return character_codes[0]
        return None

def _download_and_link(character_id, user_id,sound_url):
    sound_data = _download(sound_url)
    if not sound_data:
        return
    sound_id = _add_data(sound_data, user_id)
    if not sound_id:
        return
    _link(user_id, character_id, sound_id)

def _download(sound_url):
    try:
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0"
        headers = {"User-Agent": user_agent}
        url_request = urllib.request.Request(sound_url, headers=headers)
        response = urllib.request.urlopen(url_request)
        sound_data = response.read()
        return sound_data
    except Exception as e:
        error_msg = " ".join(["Error when accessing",sound_url,str(e)])
        config.service_factory.get_log_service().error(error_msg)
    return None

def _add_data(sound_data, user_id):
    sound_service = config.service_factory.get_sound_service()
    sound_id = sound_service.add(sound_data, user_id)
    return sound_id

def _link(user_id, character_id, sound_id):
    character_sound_service = config.service_factory.get_character_sound_service()
    character_sound_service.link(user_id, character_id, sound_id)

def retrive_sound_and_link(character_code, character_id, user_id):
    sound_download_urls = ["http://translate.google.com.hk/translate_tts?ie=UTF-8&tl=en&q=",
                           "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q="]
    for download_url in sound_download_urls:
        sound_url = download_url + character_code
        _download_and_link(character_id, user_id, sound_url)
        time.sleep(3)

def download_sound(character_code, character_id, user_id):
    try:
        executor = concurrent.futures.ThreadPoolExecutor(2)
        executor.submit(retrive_sound_and_link, character_code, character_id, user_id)
    except Exception as e:
        config.service_factory.get_log_service().error(str(e))
    finally:
        executor.shutdown(False)