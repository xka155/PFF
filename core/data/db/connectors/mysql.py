import pymysql

''' Connector to a underlying MySQL database server.
    Used by Data Access Layer modules
'''


class MySQLConnecter:
    '''
        Class representing a connection to an mysql database

        Params:
            username (str): username of mysql server
            password (str): password of mysql server
            host (str): hostname of mysql server
            database (str): database name of mysql server

        Attributes:
            username (str): username of mysql server
            password (str): password of mysql server
            host (str): hostname of mysql server
            database (str): database name of mysql server
            cursor (obj): cursor constructed from db connection

    '''

    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.hostname = host
        self.database = pymysql.connect(host=self.hostname, user=self.username,
                                        passwd=self.password, db=database)
        self.cursor = self.database.cursor()

    # Executes query. Args: query(str), params(tuple)
    def execute_query(self, query, params):
        print(query)
        self.cursor.execute(query, params)

        rows = self.cursor.fetchall()

        if len(rows) > 0:
            return rows

    def commit_query(self):
        self.database.commit()
