import numpy as np # linear algebra
import pandas as pd #data processing

import os
import re
import nltk
from sklearn.feature_extraction import stop_words


def get_all_query(title, author, text):
    total= title + author + text
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence, s=None):
    filter_sentence = ''
    lemmatizer= nltk.WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]','',s)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
