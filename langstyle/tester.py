#!/usr/bin/env python

import unittest
from . import config
from . import test
from .test import unit
from .test.unit import character_service_test
from .test.unit import user_character_service_test
from .test.unit import image_service_test

def run():
    """discover all unit tests, and run"""

    test_suite = unittest.TestSuite()
    
    #all_tests = _load_from_test_case()
    all_tests = _load_all()
    test_suite.addTests(all_tests)
    unittest.TextTestRunner().run(all_tests)

def _load_all():
    test_loader = unittest.TestLoader()
    return test_loader.discover("test","*test.py", config.ROOT_DIRECTORY)

def _load_from_test_case():
    test_loader = unittest.TestLoader()
    #test_case_module = test.unit.user_character_service_test
    #test_case_module = test.unit.character_service_test
    test_case_module = test.unit.image_service_test
    return test_loader.loadTestsFromModule(test_case_module)
    #test_case_class = test.unit.user_character_service_test.GetCurrentTest
    #test_case_class = test.unit.user_character_service_test.GetLearningTest
    #test_case_class = test.unit.user_character_service_test.NextTest
    #test_case_class = test.unit.user_character_service_test.GetCountTest
    #test_case_class = test.unit.user_character_service_test.GetGraspTest
    #test_case_class = test.unit.character_service_test.AddTest
    #test_case_class = test.unit.character_service_test.GetIdTest
    #test_case_class = test.unit.character_service_test.GetTest
    #test_case_class = test.unit.image_service_test.AddTest
    #test_case_class = test.unit.image_service_test.GetTest
    #return test_loader.loadTestsFromTestCase(test_case_class)

if __name__ == '__main__':
    run()