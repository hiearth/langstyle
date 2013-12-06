#!/usr/bin/env python

from mysql import connector as dbconnector
from . import base_repository

class CharacterRepository(base_repository.BaseRepository):

    def add(self, word_character):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            result = cursor.callproc("WordCharacter_I",(word_character, None))
            return result[1]
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        return None

    def get(self, character_id):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            cursor.callproc("WordCharacter_S_By_Id", [character_id])
            return self._fetch_one(cursor)
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.close()

    def get_id(self, word_character):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            cursor.callproc("WordCharacter_S_By_Code", [word_character])
            return self._fetch_one(cursor)
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.close()

    def _fetch_one(self,cursor):
        for result in cursor.stored_results():
            first_result = result.fetchone()
            if first_result:
                return first_result[0]
        return None