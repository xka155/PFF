'''
    Parsers for csv files

'''


def wiki_ticker_parser(data):
    result = []

    for row in data:
        wiki_ticker = row[0]
        result.append((wiki_ticker.split('/'))[1])

    return result
