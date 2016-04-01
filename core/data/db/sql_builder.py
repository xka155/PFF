class SQLBuilder:
    '''
        Class used to build up a parameterised SQL query string
        Implements a builder pattern.

        Params:
            None

        Attributes:
            query (str): query string that is built
            params ([str]): list of strings of values

        On build() it returns a tuple of (query, params), where query is
        already parameterised and params is a tuple of values

    '''

    def __init__(self):
        self.query = ""
        self.params = []

    def build(self):
        return (self.query, tuple(self.params))

    def insert_into(self, table, values):
        val_str = ','.join(["%s"] * len(values))

        self.query += "INSERT INTO " + table + " VALUES (" + val_str + ') '

        for v in values:
            self.params.append(v)

        return self

    def select(self, columns, table):
        self.query += "SELECT "

        for i in range(0, len(columns) - 1):
            self.query += columns[i] + ", "

        self.query += columns[len(columns) - 1] + " "

        self.query += "FROM " + table + " "

        return self

    def orderby(self, column):
        self.query += "ORDER BY " + column

        return self
