#!/usr/bin/env python3

from mysql import connector as dbconnector
from .. import config

class UserRepository:

    def __init__(self):
        pass

    def grasp(self, user_id):
        raise NotImplementedError()

    def count(self, user_id, character_id):
        raise NotImplementedError()
    
    def get_learning(self, user_id):
        learning_list = []
        try:
            con = dbconnector.connect(**config.database_connection)
            cursor = con.cursor()
            cursor.callproc("UserProgress_Learning_S",(user_id,))
            learning_list.extend([character_result["character_code"] for character_result in cursor.fetchmany()])
        except Exception as e:
            config.service_factory.get_log_service().error(e.args)
        finally:
            cursor.close()
            con.close()
        return learning_list

    def get_current_character(self, user_id):
        raise NotImplementedError()
