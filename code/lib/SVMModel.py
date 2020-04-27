import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

class SVMModel:
    def __init__(self, logging, artifacts_path):
        self.__logging = logging
        self.__artifacts_path = artifacts_path
    
    def init_model(self):
        # Create model with Scikit library
        self.__logging.info('Creating new model...')
        self.__model = Pipeline([('vect', CountVectorizer(strip_accents=None, lowercase=False)),
                                 ('svm', SGDClassifier(alpha=0.001,
                                                         loss='modified_huber',
                                                         penalty='l2',
                                                         random_state=42,
                                                         tol=0.0001))])
    
    def load_model(self, model_name):
        self.__logging.info('Loading model "%s"...' % model_name)
        filepath = self.__artifacts_path + '/' + model_name + '.pickle'
        with open(filepath, 'rb') as fp:
            self.__model = pickle.load(fp)
    
    def save_model(self, model_name):
        self.__logging.info('Saving model "%s"...' % model_name)
        filepath = self.__artifacts_path + '/' + model_name + '.pickle'
        with open(filepath, 'wb') as fp:
            pickle.dump(self.__model, fp)
    
    def train(self, df: pd.DataFrame, display_model_performance=False):
        if self.__model is None:
            raise Exception('No model loaded')
        
        X_data = df[['text']].to_numpy().reshape(-1)
        Y_data = df[['category']].to_numpy().reshape(-1)
        
        n_texts = len(X_data)
        self.__logging.info('Texts in dataset: %d' % n_texts)

        n_categories = len(self._get_categories(df))
        self.__logging.info('Number of categories: %d' % n_categories)

        self.__logging.info('Loading train dataset...')
        X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.3)
        
        self.__logging.info('Training...')
        self.__model.fit(X_train, Y_train)
        
        if display_model_performance:
            # Display accuracy and confussion matrix
            self._display_model_performance(df, X_test, Y_test)
    
    def predict(self, df):
        if self.__model is None:
            raise Exception('No model loaded')

        texts = df[['text']].to_numpy().reshape(-1)
        return self.__model.predict(texts)
    
    def _display_model_performance(self, df, X_test, Y_test):
        Y_pred = self.__model.predict(X_test)
        
        cm = confusion_matrix(Y_test, Y_pred)
        cm_norm = np.around(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], decimals=2)
        category_names = self._get_categories(df)
        cm_df = pd.DataFrame(cm_norm,
                             index=category_names, 
                             columns=category_names)
        
        self.__logging.info('Accuracy: %.4f' % accuracy_score(Y_pred, Y_test))
        self.__logging.info('Classification report:')
        self.__logging.info(classification_report(Y_test, Y_pred))
        self.__logging.info('Confussion matrix:')
        self.__logging.info(cm_df)

    def _get_categories(self, df):
        return df['category'].unique()        
