from core.data.enums.sourcesenum import DataSource
from core.data.dataset import DataSet
from core.utils.config import get_config_value

import os

'''
Class representing Quandl data source. This is used in a DataFeed.

Args:
    tables (list[enum]): List of tables (as enums) that we will use in
    this source

Attributes:
    tables (list[enum]): List of tables  that we will use in this source
    datasource (enum): Enum representing the source ie Quandl
    url (str): base url of the source
    datasets (dict[enum => obj]): objs used to query the corresponding tables

'''


class Quandl:

    def __init__(self, tables):
        self.datasets = {}
        self.base_url = "https://www.quandl.com/api/v3/datasets/"

        dirname = os.path.dirname(__file__)
        path = dirname.replace('sources', 'config/')
        path += 'api.ini'

        self.key = get_config_value(path, 'QUANDL', 'API_KEY')
        self._tables = tables
        self._datasource = DataSource.QUANDL

        for table in tables:
            self.datasets[table] = DataSet(table, self.base_url, self.key)

    def query_table(self, table, args):
        ds = self.datasets[table]
        data = ds.query(args)
        return data

    @property
    def tables(self):
        return self._tables

    @property
    def datasource(self):
        return self._datasource
