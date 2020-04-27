import pandas as pd
import numpy as np
import math
import re

import string
import spacy
from spacy.lang.en import English

class Preprocess:
    MAX_SEQUENCE_LENGTH = 1000
    
    def __init__(self, logging):
        self.__logging = logging
    
    def parse_input_data(self, input_data):
        return pd.DataFrame({'text': input_data}, columns=['text'])

    # Parse the column of data and the category, and transform them into a Pandas DataFrame to
    # work in an easier way with them
    def parse_query_result(self, query_result):
        self.__logging.info('Parsing query result...')
        result = {'text': [], 'category': []}
        for row in query_result:
            result['text'].append(row['text'])
            result['category'].append(row['category'])

        return pd.DataFrame(result, columns=['text', 'category'])

    # Remove all punctuation symbols and normalize white spaces
    def apply_char_cleaner(self, df):
        self.__logging.info('Applying char cleaner...')
        for _, row in df.iterrows():
            text = row['text']
            
            for symbol in list(string.punctuation) :
                text = text.replace(symbol, ' ')

            # Normalize white spaces
            text = re.sub(r"\s+", ' ', text)
            
            row['text'] = text
        
        return df

    # Apply lemmatization to all texts
    def apply_lemmatization(self, df: pd.DataFrame, join_char=' '):
        self.__logging.info('Applying lemmatization...')
        nlp = English()
        for _, row in df.iterrows():
            text = row['text']
            tokens = nlp(text)
            text = [ w.lemma_.strip().lower() if w.lemma_ != "-PRON-" else w.lower_ for w in tokens ]
            row['text'] = join_char.join(text)
        
        return df
    
    # Remove stop words
    def apply_stop_words(self, df: pd.DataFrame, join_char=' ', split_char=' '):
        self.__logging.info('Applying stop words remover...')
        stop_words = list(spacy.lang.en.stop_words.STOP_WORDS) + list(string.punctuation)
        for _, row in df.iterrows():
            tokens = row['text'].split(split_char)
            text = [w for w in tokens if w not in stop_words]
            row['text'] = join_char.join(text)
        
        return df

    # Apply TF-IDF formula to clean texts
    def apply_tf_idf(self, df: pd.DataFrame, split_char=' ', join_char=' '):
        self.__logging.info('Applying TF-IDF remover...')
        all_tf_idf = self._calculate_tf_idf(df, split_char)
        
        for doc_i, doc_tf_idf in enumerate(all_tf_idf):
            doc_tf_idf = {k: v for k, v in sorted(doc_tf_idf.items(), key=lambda item: item[1], reverse=True)}
            doc_tf_idf_values = np.array(list(doc_tf_idf.values()))

            print(doc_tf_idf)
            print(doc_tf_idf_values)
            probs = doc_tf_idf_values / sum(doc_tf_idf_values)
            
            p_value = 0
            for i, p in enumerate(probs):
                if p_value < 0.975:
                    p_value += p
                else:
                    break
            
            threshold = doc_tf_idf_values[i]
            
            row = df.loc[doc_i, :]
            tokens = row['text'].split(split_char)
            i = len(tokens)

            while i >= 0:
                i -= 1
                w = tokens[i]
                if doc_tf_idf[w] < threshold:
                    del tokens[i]
                
            
            doc_tf_idf = {k: v for k, v in sorted(doc_tf_idf.items(), key=lambda item: item[1])}        
            row['text'] = join_char.join(tokens)
        
        return df

    def get_max_sequence_length(self):
        return self.MAX_SEQUENCE_LENGTH

    def _calculate_tf(self, df: pd.DataFrame, split_char=' '):
        tf = []
        for _, row in df.iterrows():
            tokens = row['text'].split(split_char)
            
            words_freqs = {}
            for w in tokens:
                words_freqs[w] = 1 if w not in words_freqs else (words_freqs[w] + 1)
            
            max_freq = max(list(words_freqs.values()))
            words_freqs = {w:(abs_freq / max_freq) for w, abs_freq in words_freqs.items()}
            
            tf.append(words_freqs)
        
        print('TF:')
        print(tf)
        print('-'*10)
        
        return tf

    def _calculate_idf(self, df: pd.DataFrame, split_char=' '):
        idf = {}
        n_docs = len(df.index)
        
        count_usage = {}
        for _, row in df.iterrows():
            tokens = row['text'].split(split_char)
            
            vocabulary_in_doc = list(set(tokens))
            for w in vocabulary_in_doc:
                if w not in count_usage:
                    count_usage[w] = 1
                else:
                    count_usage[w] += 1

        print(count_usage)
        for w, count in count_usage.items():            
            idf[w] = math.log(n_docs / count)
        
        print('IDF:')
        print(idf)
        print('-'*10)
        
        return idf

    def _calculate_tf_idf(self, df: pd.DataFrame, split_char=' '):
        tf = self._calculate_tf(df, split_char)
        idf = self._calculate_idf(df, split_char)
        
        tf_idf = []
        for index, row in df.iterrows():
            tokens = row['text'].split(split_char)
            vocabulary_in_doc = list(set(tokens))
            
            row_tf_idf = {}
            for w in vocabulary_in_doc:
                row_tf_idf[w] = tf[index][w] * idf[w]
            
            tf_idf.append(row_tf_idf)
        
        return tf_idf
