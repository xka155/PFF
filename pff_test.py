from tests.data_tests import TestDataFeed, TestDataSet, TestQuandlConnection
from tests.requery_tests import TestRequeryIntegration

import unittest


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataFeed))
suite.addTest(unittest.makeSuite(TestDataSet))
suite.addTest(unittest.makeSuite(TestQuandlConnection))
suite.addTest(unittest.makeSuite(TestRequeryIntegration))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
