#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd
inputfile = '../data/data2.csv'
data = pd.read_csv(inputfile)

from sklearn.linear_model import AdaptiveLasso
model = AdaptiveLasso(gamma = 1)
model.fit(data.iloc[:,0:,6],data['y'])
model.coef_