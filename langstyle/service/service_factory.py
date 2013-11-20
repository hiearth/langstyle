#!/usr/bin/env python3

from . import character_service
from . import log_service
from . import user_service

_character_service = None
_log_service = None
_user_service = None

def get_character_service():
    if not _character_service:
        _character_service = character_service.CharacterService()