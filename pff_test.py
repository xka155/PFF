from tests.data_tests import TestDataFeed, TestDataSet, TestQuandlConnection

import unittest


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataFeed))
suite.addTest(unittest.makeSuite(TestDataSet))
suite.addTest(unittest.makeSuite(TestQuandlConnection))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
