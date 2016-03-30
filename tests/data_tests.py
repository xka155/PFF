import unittest

from core.errors.feederror import DataFeedError
from core.data.sources.quandl import Quandl
from core.data.datafeed import DataFeed
from core.data.enums.sourcesenum import TableNames
from core.data.enums.sourcesenum import DataSource


class TestDataFeed(unittest.TestCase):


    def test_raise_invalid_source(self):
        quandl = Quandl([])
        datafeed = DataFeed([quandl])

        self.assertRaises(KeyError, datafeed.query_source, "test", None)

    def test_can_query_source(self):
        quandl = Quandl([TableNames.Q_WIKI_EOD])
        datafeed = DataFeed([quandl])

        try:
            datafeed.query_source(DataSource.QUANDL, TableNames.Q_WIKI_EOD, ticker="foo")
        except:
            self.fail("Exception with correct params")

    def test_raise_no_ticker(self):
        quandl = Quandl([TableNames.Q_WIKI_EOD])
        datafeed = DataFeed([quandl])

        self.assertRaises(KeyError, datafeed.query_source, DataSource.QUANDL, TableNames.Q_WIKI_EOD)
