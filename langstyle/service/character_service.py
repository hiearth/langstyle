#!/usr/bin/env python3

from .. import config
from .. import helper

class CharacterService:

    def __init__(self,user_repository):
        self._user_repository = user_repository