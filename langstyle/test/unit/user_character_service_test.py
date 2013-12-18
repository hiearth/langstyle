#!/usr/bin/env python

import unittest
from langstyle.service import user_character_service
from .. import test_helper
from ..mock import mock_user_character_repository
#from langstyle.database import user_character_repository

class UserCharacterServiceTestCase(unittest.TestCase):

    def setUp(self):
        # get a mock user
        self._user_id = 1
        self._user_character_repository = mock_user_character_repository.MockUserCharacterRepository()
        #self._user_character_repository = user_character_repository.UserCharacterRepository()
        self._user_character_service = user_character_service.UserCharacterService(self._user_character_repository)
        self._character_ids = []

    def _add_some_learning_character(self):
        character_count = 10
        self._character_ids = test_helper.generate_some_ids(character_count)
        for character_id in self._character_ids:
            self._user_character_repository.begin_learn(self._user_id, character_id)

    def _get_random_character(self):
        raise NotImplementedError()


class GetGraspTest(UserCharacterServiceTestCase):

    def test_FirstTime_ReturnEmpty(self):
        grasp_character_ids = self._user_character_service.get_grasp(self._user_id)
        self.assertCountEqual(grasp_character_ids, [])

    def _set_some_grasp_character(self):
        self._add_some_learning_character()
        for character_id in self._character_ids:
            self._user_character_repository.mark_grasp(self._user_id, character_id)

    def test_StartButNotComplete(self):
        self._set_some_grasp_character()
        grasp_character_ids = self._user_character_service.get_grasp(self._user_id)
        self.assertCountEqual(grasp_character_ids, self._character_ids)


class GetLearningTest(UserCharacterServiceTestCase):

    def test_FirstTime_ReturnEmpty(self):
        learning_character_ids = self._user_character_service.get_learning(self._user_id)
        self.assertCountEqual(learning_character_ids, [])

    def test_StartButNotComplete(self):
        self._add_some_learning_character()
        learning_character_ids = self._user_character_service.get_learning(self._user_id)
        self.assertCountEqual(learning_character_ids, self._character_ids)



class GetCurrentTest(UserCharacterServiceTestCase):

    def test_FirstTime_ReturnNone(self):
        current_character_id = self._user_character_service.get_current_character(self._user_id)
        self.assertIsNone(current_character_id)

    def test_StartButNotComplete(self):
        self._add_some_learning_character()
        character_id = test_helper.choice(self._character_ids)
        self._user_character_repository.set_current_character(self._user_id, character_id)
        current_character_id = self._user_character_service.get_current_character(self._user_id)
        self.assertEqual(character_id, current_character_id)



class NextTest(UserCharacterServiceTestCase):
    
    def test_FirstTime(self):
        next_character_id = self._user_character_service.next(self._user_id)
        self.assertIsNone(next_character_id)

    def test_StartButNoCurrentCharacter(self):
        self._add_some_learning_character()
        next_character_id = self._user_character_service.next(self._user_id)
        self.assertIn(next_character_id, self._character_ids)

    def test_StartAndHasCurrentCharacter(self):
        self._add_some_learning_character()
        some_character_id = test_helper.choice(self._character_ids)
        self._user_character_repository.set_current_character(self._user_id, some_character_id)
        next_character_id = self._user_character_service.next(self._user_id)
        self.assertEqual(some_character_id, next_character_id)



class GetCountTest(UserCharacterServiceTestCase):

    def _get_learning_character(self):
        raise NotImplementedError()

    def test_FirstTime_ReturnZero(self):
        self._add_some_learning_character()
        some_character_id = test_helper.choice(self._character_ids)
        character_count = self._user_character_service.get_count(self._user_id, some_character_id)
        self.assertEqual(character_count, 0)

    def test_IsLearning_GreaterThanZero(self):
        self._add_some_learning_character()
        some_character_id = test_helper.choice(self._character_ids)
        self._user_character_repository.increase_count(self._user_id, some_character_id)
        character_count = self._user_character_service.get_count(self._user_id, some_character_id)
        self.assertEqual(character_count, 1)
