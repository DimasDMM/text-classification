import psycopg2 as pg
import logging
from pathlib import Path
import os
import traceback

SCHEMA_FILE = '../../schema.sql'
PATH_TXT_FILES = '../../../data/raw'

class DBConnection:
    def __init__(self, logging):
        self._logging = logging
        
    def __enter__(self):
        self._logging.info("Creating DB connection...")
        self._connection = pg.connect(
            host=os.environ['DB_HOST'],
            port=os.environ['DB_INTERNAL_PORT'],
            dbname=os.environ['DB_DBNAME'],
            user=os.environ['DB_USER']
        )
        return self._connection

    def __exit__(self, type, value, traceback):
        self._logging.info("Closing the DB connection!")
        self._connection.close()

class ETL():
    TABLE_TEXTS = 'texts'
    
    def __init__(self, logging, schema_file: str):
        self._logging = logging
        self.__init_schema(schema_file)
    
    def __init_schema(self, schema_file: str) -> None:
        with DBConnection(self._logging) as conn:
            self._logging.info("Creating schema...")
            cursor = conn.cursor()

            # Read SQL file to create schema
            current_path = os.path.dirname(os.path.abspath(__file__))
            file_path = current_path + '/' + schema_file
            fp = open(file_path, 'r')
            statements = fp.readlines()
            fp.close()

            statements = ' '.join(statements)
            cursor.execute(statements)
            
            conn.commit()
    
    def import_data(self, data_path: str) -> None:
        with DBConnection(self._logging) as conn:
            self._logging.info("Importing data...")
            cursor = conn.cursor()
            
            # The folder names are the category names
            current_path = os.path.dirname(os.path.abspath(__file__))
            data_abs_path = current_path + '/' + data_path

            if not os.path.isdir(data_abs_path):
                self._logging.error('Path of data does not exist: %s' % data_abs_path)
                raise Exception
            
            category_names = os.walk(data_abs_path)
            category_names = list(category_names)[0][1]
            
            # Import each file content with the same category name as folder name
            for category in category_names:
                p = Path(current_path + '/' + data_path + '/' + str(category))
                files = [x for x in p.iterdir() if x.is_file()]
                for f in files:
                    with open(str(f), encoding='utf-8', errors='ignore') as fp:
                        text = fp.read()
                        self.__insert_text(cursor, text, category)

            conn.commit()
            self._logging.info("Data imported!")
    
    def __insert_text(self, cursor, text: str, category: str):
        stmt = 'INSERT INTO "{}" ("text", "category") VALUES (%(text)s, %(category)s)'.format(self.TABLE_TEXTS)
        raw_values = {
            'text': text,
            'category': category
        }
        cursor.execute(stmt, raw_values)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        logging.info('## ETL SCRIPT ##')
        etl = ETL(logging, SCHEMA_FILE)
        etl.import_data(PATH_TXT_FILES)
        logging.info('ETL Finished!')
    except (Exception, pg.DatabaseError) as error:
        logging.error("Failed to import data: {}".format(error))
        traceback.print_exc()
        exit(1)
