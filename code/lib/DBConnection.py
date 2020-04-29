import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import os

class DBConnection:
    def __init__(self, connection_data, logging):
        self.__connection_data = connection_data
        self.__logging = logging

    def __enter__(self):
        self.__logging.info("Creating DB connection...")
        self.__connection = pg.connect(
            host = self.__connection_data['host'],
            port = self.__connection_data['port'],
            dbname = self.__connection_data['dbname'],
            user = self.__connection_data['user']
        )
        self.__logging.info("Connection created!")
        return self

    def __exit__(self, type, value, traceback):
        self.__logging.info("Closing the DB connection!")
        self.__connection.close()

    def cursor(self, use_real_dict=True):
        if use_real_dict:
            return self.__connection.cursor(cursor_factory=RealDictCursor)
        else:
            return self.__connection.cursor()
