#!/usr/bin/env python3

from .. import config
from .. import helper

class CharacterService:

    def __init__(self,user_repository):
        self._user_repository = user_repository

    def add(self, word_character):
        # first find whether word_character exist 
        # if exists, return the characterId
        # else, add and return the characterId
        raise NotImplementedError()

    def get(self, word_character):
        raise NotImplementedError()