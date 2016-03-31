import urllib.request
import urllib.error


class DataSet:
    '''
    Class representing a set of data. 1-1 mapping with a table in a source.
    Held by a source object.

    Params:
        table_name (enum): Name of table, configured in sourcesenum
        base_url (str): url of the providing source
        api_key (str): api key for queries

    Attributes:
        name (enum): Table name
        base (str): Base url
        key (str): Api Key

    '''

    def __init__(self, table_name, base_url, api_key):
        self.name = table_name
        self.base = base_url + '/' + table_name.value + '/'
        self.key = api_key

    def query(self, args):
        ticker = args['ticker']

        if 'type' in args:
            file_t = args['type']
        else:
            file_t = 'csv'

        query_url = self.base + ticker + '.' + file_t + '?'
        query_url += "api_key=" + self.key

        query_url = set_url_params(query_url, args)

        urllib.request.urlopen(query_url)

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
