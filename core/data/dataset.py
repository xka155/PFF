class DataSet:

    def __init__(self, table_name, base_url, api_key):
        self.name = table_name
        self.base = base_url + '/' + table_name.value + '/'
        self.key  = api_key


    def query(self, args):
        ticker = args['ticker']

        if 'type' in args:
            file_t = args['type']
        else:
            file_t = 'csv'

        query_url = self.base + ticker + '.' + file_t + '?'
        query_url += "api_key=" + self.key

        query_url = set_url_params(query_url, args)


def set_url_params(url, params):
    keys = list(params.keys())

    for i in range(0, len(keys)):
        url += '&' + keys[i] + '=' + params[keys[i]]

    return url
