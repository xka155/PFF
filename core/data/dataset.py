import urllib.request
from urllib.error import URLError, HTTPError
from datetime import datetime

import core.data.db.requery_dal as requery_dal
from core.data.csv.parsers import wiki_ticker_parser
from core.utils.config import get_tickers


class DataSet:
    '''
    Class representing a set of data. 1-1 mapping with a table in a source.
    Held by a source object.
    If query fails due to server error or no internet then we add to
    the requery table.

    Params:
        table_name (enum): Name of table, configured in sourcesenum
        base_url (str): url of the providing source
        api_key (str): api key for queries

    Attributes:
        name (enum): Table name
        base (str): Base url
        key (str): Api Key

    '''

    def __init__(self, table_name, base_url, api_key, data_source):
        self.name = table_name
        self.base = base_url + '/' + table_name.value + '/'
        self.key = api_key
        self.source = data_source

    def query_ticker(self, args):
        date = datetime.now()
        date = date.strftime('%Y-%m-%d')

        # For requery. Tidy it up?
        values = [date, str(args), ticker, self.name.value, self.source.value]
        try:
            response = urllib.request.urlopen(query_url)

            content = response.read().decode("utf-8")
            content = content.split('\n')

            data = []

            for row in content:
                data.append(row)

            return data
        except HTTPError as err:
            if str(err.code)[0] == '5':
                requery_dal.add_requery(values)
            else:
                raise
        except URLError:
            requery_dal.add_requery(values)

    def query_all(self, args):
        if 'ticker' in args:
            args.pop('ticker')
            print("Dont need a ticker...")

        tickers = get_tickers(self.name, wiki_ticker_parser)
        urls = _generate_urls(tickers, args)

    def _generate_urls(self, tickers, args):


    def _generate_url(self, args):
        query_url = self.base + ticker + '.' + file_t + '?'

        if 'ticker' in args:
            query_url += args[ticker] +

        if 'type' in args:
            file_t = args['type']
        else:
            file_t = 'csv'

        query_url += "api_key=" + self.key

        query_url = set_url_params(query_url, args)



'''
Method that takes a dictionary and adds it to the provided url as k-v url
parameters

Params:
    url (str): base url to add to
    params (dict): dictionary of key-value pairs

Returns:
    url (str): url with added url parameters

'''


def set_url_params(url, params):
    keys = list(params.keys())

    for i in range(0, len(keys)):
        url += '&' + keys[i] + '=' + params[keys[i]]

    return url
