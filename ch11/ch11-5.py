#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

discfile = '../data/discdata_processed.xls'
data = pd.read_excel(discfile,index_col='COLLECTTIME')
lagnum = 12


data = data.iloc[:len(data)-5]
xdata = data['CWXT_DB:184:D:\\']

from statsmodels.tsa.arima_model import ARIMA


arima = ARIMA(xdata,(0,1,1)).fit()
xdata_pred = arima.predict(typ = 'levels')
print(xdata_pred)
pred_error = (xdata_pred - xdata).dropna()
from statsmodels.stats.diagnostic import acorr_ljungbox

lb,p = acorr_ljungbox(pred_error,lags = lagnum)
h = (p<0.05).sum()#小于0.05非白噪声

if h > 0:
    print('模型ARIMA（0,1，1）不符合白噪声检测')
else:
    print('模型ARIMA（0,1，1）符合白噪声检测')
