#!/usr/bin/env python

from mysql import connector as dbconnector
from .. import config

class UserCharacterRepository:

    def __init__(self):
        pass

    def _create_connection(self):
        return dbconnector.connect(**config.database_connection)

    def _log_error(self, error):
        config.service_factory.get_log_service().error(error.msg)

    def grasp(self, user_id):
        grasp_list= []
        try:
            con = self._create_connection()
            cursor = con.cursor()
            cursor.callproc("UserProgress_Grasp_S", [user_id])
            while True:
                fetched_results = cursor.fetchmany()
                if not fetched_results:
                    break
                grasp_list.extend([character_result["CharacterCode"]
                                   for character_result in fetched_results])
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            con.close()
        return grasp_list

    def count(self, user_id, character_id):
        character_count = 0
        try:
            con = self._create_connection()
            cursor = con.cursor()
            cursor.callproc("UserProgress_Count_S", [user_id, character_id])
            count_result = cursor.fetchone()
            if count_result:
                character_count = count_result["RepeatCount"]
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            con.close()
        return character_count
    
    def get_learning(self, user_id):
        learning_list = []
        try:
            con = self._create_connection()
            cursor = con.cursor()
            cursor.callproc("UserProgress_Learning_S",[user_id])
            while True:
                fetched_results = cursor.fetchmany()
                if not fetched_results:
                    break
                learning_list.extend([character_result["CharacterCode"] 
                                      for character_result in fetched_results])
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            con.close()
        return learning_list

    def get_current_character(self, user_id):
        current_character = None
        try:
            con = self._create_connection()
            cursor = con.cursor()
            cursor.callproc("UserCurrentCharacter_S", [user_id])
            character_result = cursor.fetchone()
            if character_result:
                current_character = character_result["CharacterCode"]
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            con.close()
        return current_character
        