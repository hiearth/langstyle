#!/usr/bin/env python

from mysql import connector as dbconnector
from . import base_repository
from .. import helper

class CharacterRepository(base_repository.BaseRepository):

    def add(self, word_character):
        result = self._call_proc_non_query("WordCharacter_I",(word_character, None))
        if result:
            return result[1]
        return None

    def get(self, character_id):
        result = self._call_proc_query_one("WordCharacter_S_By_Id", [character_id])
        if result:
            return result[0]
        return None

    def get_id(self, word_character):
        similar_characters = self._call_proc_query_all("WordCharacter_S_By_Code", [word_character])
        exact_match_character = helper.find_first(similar_characters, 
            (lambda character: character[1] == word_character))
        if exact_match_character:
            return exact_match_character[0]
        return None
