#!/usr/bin/env python

from .. import config
from .. import helper

class SoundService:

    def __init__(self, sound_repository, sound_file_service):
        self._sound_repository = sound_repository
        self._sound_file_service = sound_file_service

    def get(self, sound_id):
        sound_item = self._sound_repository.get(sound_id)
        if sound_item:
            return self._sound_file_service.read(sound_item.md5)
        return None

    def get_key(self, sound_id):
        sound_item = self._sound_repository.get(sound_id)
        if sound_item:
            return sound_item.md5
        return None

    def add(self, sound_data, user_provider_id):
        sound_md5 = helper.md5_hash(sound_data)
        try:
            self._sound_file_service.write(sound_md5, sound_data)
            sound_id = self._sound_repository.add(sound_md5, user_provider_id)
            return sound_id
        except Exception as e:
            config.service_factory.get_log_service().error(str(e))
        return None