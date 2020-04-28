'''
Created on Apr 28, 2020

@author: Dell
'''
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

all_data = pd.read_csv(r"E:/posts_matrix.csv")
all_data = all_data.dropna(subset=['word_count'])
all_data.reset_index(inplace=True, drop=True)
print(all_data)

all_data['fb'] =  all_data['comments'] + all_data['likes'] + all_data['shares']

features=all_data[['fb','word_count','title_word_count','img_count']]
labels=np.array(features['fb'])
features=features.drop('fb',axis=1)
features=np.array(features)
print(features,labels)

#splitting train and test set
train_features, test_features, train_labels, test_labels = train_test_split(features,labels,test_size=0.3)
print("Train features Shape : ",train_features.shape)
print("Test features Shape  : ",test_features.shape)
print("Train labels Shape   : ",train_labels.shape)
print("Test labels Shape    : ",test_labels.shape)

rfc = RandomForestRegressor(n_estimators=1000, max_depth=10, random_state=3)#, class_weight='balanced')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
rfc.fit(train_features, train_labels)
pred_labels = rfc.predict(test_features)
print(np.sqrt(np.mean((pred_labels-test_labels)**2))/np.mean(test_labels))


