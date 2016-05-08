import configparser
import csv
import os


# Params: abs file path, file section and its key
def get_config_value(conf_file, section, key):
    config = configparser.ConfigParser()
    config.read(conf_file)

    return config[section][key]


def get_tickers(table, fn):
    dirname = os.path.dirname(__file__)
    path = dirname.replace('utils', 'data/csv/')
    path += table.value + "-TICKERS.csv"

    data = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return fn(data)
