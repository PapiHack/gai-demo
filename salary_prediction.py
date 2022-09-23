import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_csv('salary.csv')

data['experience'].fillna(0, inplace=True)

data['test_score'].fillna(data['test_score'].mean(), inplace=True)
data['interview_score'].fillna(data['interview_score'].mean(), inplace=True)

X = data.iloc[:, :3]

# Converting the categorical feature to number 
def convert_into_int(word):
    word_conv = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
                 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
                 'fourteen':14, 'fifteen':15, 'zero':0, 0:0}
    return word_conv[word]

X['experience'] = X['experience'].apply(lambda x: convert_into_int(x))

y = data.iloc[:, -1]

lr = LinearRegression()
lr.fit(X,y)

# Serving the model 

pickle.dump(lr, open('model.pkl', 'wb'))    