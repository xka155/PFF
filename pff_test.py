from tests.data_tests import *

import unittest


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataFeed))
runner = unittest.TextTestRunner()
runner.run(suite)
