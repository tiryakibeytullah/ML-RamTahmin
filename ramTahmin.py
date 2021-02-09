import joblib
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from sklearn.compose import ColumnTransformer

def tahmin(ramTahmin):
    jlb = joblib.load('ram-model.pkl')
    model_columns = joblib.load('ram-model-kolonlari.pkl')
    print("Models Loaded")
    query = pd.get_dummies(pd.DataFrame(ramTahmin))
    query = query.reindex(columns=model_columns, fill_value=0)
    prec = list(jlb.predict(query))
    prec = prec[0][0]
    if prec < 0:
        prec = prec*-1
    print(prec)
    return prec
