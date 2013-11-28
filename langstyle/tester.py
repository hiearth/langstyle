#!/usr/bin/env python3

import unittest
from . import config
from . import test
from .test import unit
from .test.unit import character_service_test

def run():
    """discover all unit tests, and run"""

    test_suite = unittest.TestSuite()
    
    all_tests = _load_from_test_case()
    #all_tests = _load_all()
    test_suite.addTests(all_tests)
    unittest.TextTestRunner().run(test_suite)

def _load_all():
    test_loader = unittest.TestLoader()
    return test_loader.discover("test","*test.py", config.ROOT_DIRECTORY)

def _load_from_test_case():
    test_loader = unittest.TestLoader()
    return test_loader.loadTestsFromTestCase(test.unit.character_service_test.AddTest)

if __name__ == '__main__':
    run()