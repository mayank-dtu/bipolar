'''
Created on Apr 28, 2020

@author: Dell
'''
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2 
import numpy as np
from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import re
    
def text_from_html(x):
    try:
        response = urllib2.urlopen(x)
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        return soup.get_text()
    except:
        return None

def get_word_count(x):
    if not x is None:
        return len(x.split(' '))
    else:
        return None
from nltk.util import ngrams
from nltk.corpus import stopwords
import re

def get_word_stats(txt_series, n, rem_stops=False):
    txt_words = []
    txt_len = []
    for w in txt_series:
        if w is not None:
            if rem_stops == False:
                word_list = [x for x in ngrams(re.findall('[a-z0-9\']+', w.lower()), n)]
            else:
                word_list = [y for y in ngrams([x for x in re.findall('[a-z0-9\']+', w.lower())\
                                                if x not in stopwords.words('english')], n)]
            word_list_len = len(list(word_list))
            txt_words.extend(word_list)
            txt_len.append(word_list_len)
    return pd.Series(txt_words).value_counts().to_frame('count'), pd.DataFrame(txt_len, columns=['count'])
    
df = pd.read_csv(r"E:/posts.csv")
df = df.assign(time = pd.to_datetime(df['time'], dayfirst=True))
print(df)
df = df.assign(complete_text = df['link'].map(text_from_html))
print(df)
df['img_count'] = np.where(df['image'].isnull(), 0, 1)
print(df)
df = df.assign(word_count = df['complete_text'].map(get_word_count))
df = df.assign(title_word_count = df['post_text'].map(get_word_count))
print(df[['complete_text','word_count','title_word_count']][::-1])

hw,hl = get_word_stats(df['post_text'], 3, 1)
print(hw)

hw,hl = get_word_stats(df['complete_text'], 3, 1)
print(hw)

df.to_csv(r"E:/posts_matrix.csv")