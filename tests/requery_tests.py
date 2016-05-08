import unittest
from datetime import datetime
from unittest.mock import patch
from urllib.error import URLError, HTTPError

import core.data.dataset as dataset
from core.data.enums.sourcesenum import TableNames, DataSource


@patch('core.data.db.requery_dal.add_requery')
@patch('core.data.dataset.urllib.request.urlopen')
class TestRequeryIntegration(unittest.TestCase):

    def test_requery_added_no_connection(self, mockUrlOpen, mockAddReQuery):
        ds = dataset.DataSet(TableNames.Q_WIKI_EOD,
                             "https://www.quandl.com/api/v3/datasets/",
                             "5Fa6uDiy3SzmtRdSM7es",
                             DataSource.QUANDL)

        mockUrlOpen.side_effect = URLError("Mocking error")

        ds.query_ticker({'ticker': "BA"})

        self.assertTrue(mockAddReQuery.called)

    def test_requery_added_server_error(self, mockUrlOpen, mockAddReQuery):
        ds = dataset.DataSet(TableNames.Q_WIKI_EOD,
                             "https://www.quandl.com/api/v3/datasets/",
                             "5Fa6uDiy3SzmtRdSM7es",
                             DataSource.QUANDL)

        mockUrlOpen.side_effect = HTTPError(
                                    "https://www.quandl.com/api/v3/datasets/",
                                    500, "Internal server", None, None)

        ds.query_ticker({'ticker': "BA"})

        date = datetime.now()
        date = date.strftime('%Y-%m-%d')

        mockAddReQuery.assert_called_with([date, str({'ticker': "BA"}), "BA",
                                          TableNames.Q_WIKI_EOD.value,
                                          DataSource.QUANDL.value])

    def test_requery_not_added(self, mockUrlOpen, mockAddReQuery):
        ds = dataset.DataSet(TableNames.Q_WIKI_EOD,
                             "https://www.quandl.com/api/v3/datasets/",
                             "5Fa6uDiy3SzmtRdSM7es",
                             DataSource.QUANDL)

        ds.query_ticker({'ticker': "BA"})

        self.assertFalse(mockAddReQuery.called)
