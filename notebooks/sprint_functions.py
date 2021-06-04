import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import pickle

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score,roc_curve, auc, confusion_matrix, classification_report
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity
from sklearn.preprocessing import MinMaxScaler



def explore_data(df):
    print("**** Dimensions or Shape (rows x columns)")
    print(df.shape)
    print("**** Column Names")
    print(df.columns)
    print("**** Data Types")
    print(df.dtypes)
    print("**** Descriptive Statistics")
    print(df.describe())
    print("**** Head")
    print(df.head())
    print("**** Null Checks")
    print(df.isnull().sum())
    return df.shape, df.columns, df.dtypes, df.describe(), df.head(), df.isnull().sum()
    
def save_model(fname, model):
    """
        fname: path/filename.pkl
        model: model
        
        Saves model to a pickle file
    """
    file = open(fname, 'wb')
    
    pickle.dump(model, file)
    
    file.close()
    
    
def load_model(fname):
    """
        fname: path/filename.pkl
        Loads a model
    """
    file = open(fname, 'rb')
    data = pickle.load(file)
    file.close()
    
    return data
    