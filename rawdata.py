'''
Created on Apr 25, 2020

@author: Dell
'''
from facebook_scraper import get_posts
import pandas as pd

df=pd.DataFrame()
for post in get_posts('FoxNews',pages =1):
    print(post)
    df=df.append(post, ignore_index=True)

df.to_csv(r"E:/lol.csv")       