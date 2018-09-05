import pickle

import numpy as np
import pandas as pd
from scipy.stats import skew

loaded_model = pickle.load(open("data/model.pickle", "rb"))


def predict(test):
    train = pd.read_csv('./data/train.csv')

    train = train[~((train['GrLivArea'] > 4000) & (train['SalePrice'] < 300000))]

    all_data = pd.concat((train.loc[:,'MSSubClass':'SaleCondition'],
                        test.loc[:,'MSSubClass':'SaleCondition']))

    # drop some features to avoid multicollinearity
    all_data.drop(['1stFlrSF', 'GarageArea', 'TotRmsAbvGrd'], axis=1, inplace=True)

    train["SalePrice"] = np.log1p(train["SalePrice"])

    numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index

    skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna())) #compute skewness
    skewed_feats = skewed_feats[skewed_feats > 0.65]
    skewed_feats = skewed_feats.index

    all_data[skewed_feats] = np.log1p(all_data[skewed_feats])

    all_data = pd.get_dummies(all_data)

    all_data = all_data.fillna(all_data.mean())

    X_train = all_data[:train.shape[0]]
    X_test = all_data[train.shape[0]:]
    y = train.SalePrice

    return np.expm1(loaded_model.predict(X_test))
