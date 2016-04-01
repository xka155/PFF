import unittest

from urllib.error import HTTPError

from core.data.sources.quandl import Quandl
from core.data.datafeed import DataFeed
from core.data.dataset import set_url_params
from core.data.enums.sourcesenum import TableNames
from core.data.enums.sourcesenum import DataSource

''' TODO: Fake end point -> test integrated correctness '''


class TestDataFeed(unittest.TestCase):

    def test_raise_invalid_source(self):
        quandl = Quandl([])
        datafeed = DataFeed([quandl])

        self.assertRaises(KeyError, datafeed.query_source, "test", None)

    def test_raise_no_ticker(self):
        quandl = Quandl([TableNames.Q_WIKI_EOD])
        datafeed = DataFeed([quandl])

        self.assertRaises(KeyError, datafeed.query_source, DataSource.QUANDL,
                          TableNames.Q_WIKI_EOD)


class TestDataSet(unittest.TestCase):

    def test_format_url_correctly(self):
        base_url = "https:www.test.com/k=1"

        params_1 = {'foo': 'bar', 'hello': 'world'}

        self.assertTrue(set_url_params(base_url, params_1) ==
                        'https:www.test.com/k=1&foo=bar&hello=world')

    def test_format_url_empty_value(self):
        base_url = "https:www.test.com/k=1"

        params_1 = {'loo': ' '}

        self.assertTrue(set_url_params(base_url, params_1) ==
                        'https:www.test.com/k=1&loo= ')

    def test_format_url_no_params(self):
        base_url = "https:www.test.com/k=1"

        params_1 = {}

        self.assertTrue(set_url_params(base_url, params_1) ==
                        'https:www.test.com/k=1')

    def test_malformed_query_throws_http_error(self):
        quandl = Quandl([TableNames.Q_WIKI_EOD])
        datafeed = DataFeed([quandl])

        self.assertRaises(HTTPError, datafeed.query_source, DataSource.QUANDL,
                          TableNames.Q_WIKI_EOD, ticker="alkdsjasd")


class TestQuandlConnection(unittest.TestCase):

    def test_quandl_server_connection(self):
        quandl = Quandl([TableNames.Q_WIKI_EOD])
        datafeed = DataFeed([quandl])

        try:
            datafeed.query_source(DataSource.QUANDL, TableNames.Q_WIKI_EOD,
                                  ticker='BA')
        except HTTPError as err:
            if err.code == 500:
                self.fail("Server error")
            else:
                self.fail("Http error")
