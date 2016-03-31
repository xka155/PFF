"""
Module contains the DataFeed class implementation
DataFeed 1 -> * DataSource
"""


class DataFeed:

    '''
    Class representing a datafeed. This is the main access point for data
    providers. It contains all datasources it needs and delegates queries to
    them.

    Params:
        datasources (list[Obj]): list of datasources initialised as DataSource
        objs

    Attributes:
        sources (dict(Enum => Obj)): Dictionary of datasources

    Raises:
        query_source (KeyError): Raises KeyError if datasource is not
        valid/present

    '''

    def __init__(self, datasources):
        self.sources = {}

        # Setup dictionary of {Src (Enum) => DataSource (Obj)}
        for s in datasources:
            self.sources[s.datasource] = s

    def query_source(self, source, table, **kwargs):
        source = self.sources[source]
        data = source.query_table(table, kwargs)

        return data
