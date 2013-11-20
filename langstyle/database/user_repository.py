#!/usr/bin/env python3

class UserRepository:

    def __init__(self):
        pass

    def grasp(self, user_id):
        raise NotImplementedError()

    def count(self, user_id, character_id):
        raise NotImplementedError()
    
    def get_learning(self, user_id):
        #procedureName = "UserProcess_Learning_S"

        raise NotImplementedError()

    def get_current_character(self, user_id):
        raise NotImplementedError()
