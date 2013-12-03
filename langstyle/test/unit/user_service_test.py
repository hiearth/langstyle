#!/usr/bin/env python

import unittest
from langstyle.service import user_service
from .. import test_helper
from ..mock import mock_user_repository

class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        # get a mock user
        self._user_id = 1
        self._user_repository = mock_user_repository.MockUserRepository()
        self._user_service = user_service.UserService(self._user_repository)

    def _get_random_character(self):
        raise NotImplementedError()


class GraspTest(UserServiceTestCase):

    def setUp(self):
        super().setUp()
        self._character_ids = []

    def test_FirstTime_ReturnEmpty(self):
        grasp_character_ids = self._user_service.grasp(self._user_id)
        self.assertCountEqual(grasp_character_ids, [], "Should not grasp any character")

    def _add_some_grasp_character(self):
        character_count = 10
        self._character_ids = test_helper.generate_some_character_ids(character_count)
        for character_id in self._character_ids:
            self._user_repository.mark_grasp(self._user_id, character_id)

    def test_StartButNotComplete(self):
        self._add_some_grasp_character()
        grasp_character_ids = self._user_service.grasp(self._user_id)
        self.assertCountEqual(grasp_character_ids, self._character_ids, "grasp return wrong list")


class CharacterLearningTest(UserServiceTestCase):

    def setUp(self):
        super().setUp()
        self._character_ids = []

    def _get_in_learing_max_count(self):
        raise NotImplementedError()

    def test_FirstTime_ReturnEmpty(self):
        learning_character_ids = self._user_service.get_learning(self._user_id)
        self.assertCountEqual(learning_character_ids, [], "Should not has any learning character")

    def _add_some_learning_character(self):
        character_count = 10
        self._character_ids = test_helper.generate_some_character_ids(character_count)
        for character_id in self._character_ids:
            self._user_repository.begin_learn(self._user_id, character_id)

    def test_StartButNotComplete(self):
        self._add_some_learning_character()
        learning_character_ids = self._user_service.get_learning(self._user_id)
        self.assertCountEqual(learning_character_ids, self._character_ids, "get learning return wrong list")


class NextTest(UserServiceTestCase):
    
    def test_FirstTime(self):
        # make the user has no learning record
        next_character = self._user_service.next(self._user_id)
        # assert next_character 
        self.fail("no assertion yet")

    def test_StartButNotComplete(self):
        # make the user has some learning records
        next_character = self._user_service.next(self._user_id)
        # assert next_character 
        self.fail("no assertion yet")

    def test_Complete_ReturnNone(self):
        # make user has full learning records
        next_character = self._user_service.next(self._user_id)
        # assert next_character 
        self.fail("no assertion yet")



class CharacterCountTest(UserServiceTestCase):

    def _get_learning_character(self):
        raise NotImplementedError()

    def test_FirstTime_ReturnZero(self):
        # make the user has no learning record
        character_id = self._get_random_character()
        character_count = self._user_service.count(self._user_id, character_id)
        # assert character_count equal 0
        self.fail("no assertion yet")

    def test_IsLearning_GreaterThanOne(self):
        # make the user has some learning records
        character_id = self._get_learning_character()
        character_count = self._user_service.count(self._user_id, character_id)
        # assert character_count > 1
        self.fail("no assertion yet")

    def test_Complete_GreaterThanOne(self):
        # make user has full learning records
        character_id = self._get_random_character()
        character_count = self._user_service.count(self._user_id, character_id)
        # assert character_count > 1
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
