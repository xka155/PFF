import os

from core.utils.config import get_config_value
from core.data.db.connectors.mysql import MySQLConnecter
from core.data.db.sql_builder import SQLBuilder

'''
    Data access abstraction layer for the missed queries Table that is
    updated when we receive a 5xx error code when querying the source.
    This table will periodically be used to requery and remove if successful

'''

dirname = os.path.dirname(__file__)
path = dirname + '/config/mysql.ini'

user = get_config_value(path, 'MySQL', 'User')
pswd = get_config_value(path, 'MySQL', 'Password')
host = get_config_value(path, 'MySQL', 'Host')
db = get_config_value(path, 'MySQL', 'DB')

connector = MySQLConnecter(user, pswd, host, db)

table = get_config_value(path, 'MySQLTABLES', 'Requery')


def add_requery(values):
    builder = SQLBuilder()
    builder.insert_into(table, values)

    query, params = builder.build()

    connector.execute_query(query, params)
