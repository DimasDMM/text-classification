import pandas as pd
import logging
import sys
import os

from lib.DBConnection import DBConnection
from lib.DBData import DBData
from lib.Preprocess import Preprocess
from lib.ModelFactory import ModelFactory
from lib.SVMModel import SVMModel

ARTIFACTS_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../artifacts/"

def predict(logging, texts):
    # Preprocess the data as a pipeline
    preprocess = Preprocess(logging)
    df = preprocess.parse_input_data(texts)
    df = preprocess.apply_char_cleaner(df)
    df = preprocess.apply_lemmatization(df)

    # Load model and make predictions
    model_factory = ModelFactory(logging, ARTIFACTS_PATH)
    svm_model = model_factory.make('svm')
    
    svm_model.load_model('svm')
    predictions = svm_model.predict(df)
    
    return [p for p in predictions]

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info('## TEXT PREDICTION ##')
    
    if len(sys.argv) < 2:
        raise Exception('No texts provided!')
    
    predictions = predict(logging, sys.argv[1:])
    for p in predictions:
        print(p)
