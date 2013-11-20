#!/usr/bin/env python3

import unittest
from langstyle.service import user_service
from langstyle.database import user_repository
from langstyle.service import service_context
from langstyle.database import repository_context

class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        # get a mock user
        self._user_id = 1
        self._user_repository = user_repository.UserRepository()
        self._user_service = user_service.UserService(self._user_repository)


class GraspTest(UserServiceTestCase):

    def test_FirstTime_ReturnEmpty(self):
        # make the user has no learning record
        grasp_characters = self._user_service.grasp(self._user_id)
        # assert grasp_characters Empty
        self.fail("no assertion yet")

    def test_StartButNotComplete(self):
        # make the user has some learning records
        grasp_characters = self._user_service.grasp(self._user_id)
        # assert grasp_characters
        self.fail("no assertion yet")

    def test_Complete_ReturnAllCharacters(self):
        # make user has full learning records
        grasp_characters = self._user_service.grasp(self._user_id)
        # assert grasp_characters is the same as all character list
        self.fail("no assertion yet")


class CharacterCountTest(UserServiceTestCase):

    def _get_random_character(self):
        # reurn a random
        pass

    def _get_learning_character(self):
        pass

    def test_FirstTime_ReturnZero(self):
        # make the user has no learning record
        character = self._get_random_character()
        character_count = self._user_service.count(self._user_id, character)
        # assert character_count equal 0
        self.fail("no assertion yet")

    def test_IsLearning_GreaterThanOne(self):
        # make the user has some learning records
        character = self._get_learning_character()
        character_count = self._user_service.count(self._user_id, character)
        # assert character_count > 1
        self.fail("no assertion yet")
         
    def test_Complete_GreaterThanOne(self):
        # make user has full learning records
        character = self._get_random_character()
        character_count = self._user_service.count(self._user_id, character)
        # assert character_count > 1
        self.fail("no assertion yet")


class CharacterLearningTest(UserServiceTestCase):

    def _get_in_learing_max_count(self):
        pass

    def test_FirstTime_ReturnEmpty(self):
        # make the user has no learning record
        learning_characters = self._user_service.get_learning(self._user_id)
        # assert learning_characters is empty
        self.fail("no assertion yet")

    def test_StartButNotComplete(self):
        # make the user has some learning records
        learning_characters = self._user_service.get_learning(self._user_id)
        max_count = self._get_in_learing_max_count()
        # assert learning_characters is not empty and less than max in learning
        # count
        self.fail("no assertion yet")

    def test_Complete_ReturnEmpty(self):
        # make user has full learning records
        learning_characters = self._user_service.get_learning(self._user_id)
        # assert learning_characters is empty
        self.fail("no assertion yet")


class CurrentCharacterTest(UserServiceTestCase):

    def test_FirstTime_ReturnNone(self):
        # make the user has no learning record
        current_character = self._user_service.get_current_character(self._user_id)
        # assert current_character is None
        self.fail("no assertion yet") 

    def test_StartButNotComplete(self):
        # make the user has some learning records
        current_character = self._user_service.get_current_character(self._user_id)
        # assert current_character not None
        self.fail("no assertion yet") 

    def test_Complete_ReturnNone(self):
        # make user has full learning records
        current_character = self._user_service.get_current_character(self._user_id)
        # assert current_character is None 
        self.fail("no assertion yet") 