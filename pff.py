from core.data.datafeed import DataFeed
from core.data.enums.sourcesenum import TableNames
from core.data.enums.sourcesenum import DataSource
from core.data.sources.quandl import Quandl
from urllib.error import HTTPError

''' Entry Point '''

quandl = Quandl([TableNames.Q_WIKI_EOD, TableNames.Q_SF0_FUND,
                TableNames.Q_YFINANCE])
datafeed = DataFeed([quandl])

try:
    datafeed.query_source(DataSource.QUANDL,
                          TableNames.Q_WIKI_EOD, ticker='la')
except HTTPError as e:
    print("Fuck this connection")
    print(e)
