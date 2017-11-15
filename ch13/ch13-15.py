#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd
inputfile = '../data/data5.csv'
data = pd.read_csv(inputfile)

from sklearn.linear_model import AdaptiveLasso
model = AdaptiveLasso(gamma = 1)
model.fit(data.iloc[:,0:7],data['y'])
model.coef_