from core.data.sources.quandl import Quandl
from core.data.datafeed import DataFeed
from core.data.enums.sourcesenum import TableNames
from core.data.enums.sourcesenum import DataSource



''' Entry Point '''
quandl   = Quandl([TableNames.Q_WIKI_EOD, TableNames.Q_SF0_FUND,
                    TableNames.Q_YFINANCE])
datafeed = DataFeed([quandl])

datafeed.query_source(DataSource.QUANDL, TableNames.Q_WIKI_EOD, ticker='la')
