from enum import Enum

'''
Data sources for the feeds

'''


class DataSource(Enum):
    QUANDL = "Quandl"
    YAHOO = "Yahoo"


'''
Table sources.

Attributes:
    Q_*: Table located in the Quandl DB

'''


class TableNames(Enum):
    Q_WIKI_EOD = "WIKI"
    Q_SF0_FUND = "SF0"
    Q_YFINANCE = "YAHOO"
