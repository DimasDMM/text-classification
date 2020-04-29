import pandas as pd
import logging
import os

from lib.DBConnection import DBConnection
from lib.DBData import DBData
from lib.Preprocess import Preprocess
from lib.ModelFactory import ModelFactory
from lib.SVMModel import SVMModel

ARTIFACTS_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../artifacts/"

def train(logging):
    connection_data = {
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_INTERNAL_PORT'],
        'dbname': os.environ['DB_DBNAME'],
        'user': os.environ['DB_USER']
    }
    
    with DBConnection(connection_data, logging) as connection:
        # Get complaints data
        cursor = connection.cursor()
        dbdata = DBData(cursor, logging)
        raw_data = dbdata.get_data()

    # Preprocess the data as a pipeline
    preprocess = Preprocess(logging)
    df = preprocess.parse_query_result(raw_data)
    df = preprocess.apply_char_cleaner(df)
    df = preprocess.apply_lemmatization(df)
    df = preprocess.apply_tf_idf(df)

    # Use the processed data to train our model
    model_factory = ModelFactory(logging, ARTIFACTS_PATH)
    svm_model = model_factory.make('svm')
    
    svm_model.init_model()
    svm_model.train(df, True)
    svm_model.save_model('svm')
    
    logging.info('Done!')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info('## TRAIN MODEL ##')
    train(logging)
