import mysql.connector
import uuid


class SQLExecute(object):
    # TODO: databases_query
    databases_query = """show databases;"""

    # TODO: tables_query
    tables_query = """show tables;"""

    # TODO: tables_columns_query
    # would getting a table, first column is tableName and second column is columnName
    # a row represent which table contains what column.
    table_columns_query = """
    """

    # TODO: functions_query
    functions_query = """
    """

    # TODO: __init__
    def __init__(self, database):
        pass

    def connect(self, database=None):
        pass

    def run(self, statement):
        """Execute the sql in the database and return the results. The results
        are a list of tuples. Each tuple has 4 values
        (title, rows, headers, status).
        pass"""
        pass

    def get_result(self, cursor):
        """Get the current result's data from the cursor."""
        pass

    def tables(self):
        """Yields table names"""
        pass

    def table_columns(self):
        """Yields column names"""
        pass

    def databases(self):
        pass

    def functions(self):
        """Yields tuples of (schema_name, function_name)"""
        pass

    def show_candidates(self):
        pass

    def server_type(self):
        pass

    def get_connection_id(self):
        pass

    def reset_connection_id(self):
        pass
