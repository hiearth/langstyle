#!/usr/bin/env python3

import unittest
from . import config

def run():
    """discover all unit tests, and run"""

    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    
    all_tests = test_loader.discover("test","*test.py", config.ROOT_DIRECTORY)
    test_suite.addTests(all_tests)
    unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    run()