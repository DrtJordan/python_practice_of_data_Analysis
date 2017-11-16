#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

discfile = '../data/discdata_processed.xls'
data = pd.read_excel(discfile)

data = data.iloc[:len(data) - 5]

from statsmodels.tsa.stattools import adfuller as ADF

diff = 0
adf = ADF(data['CWXT_DB:184:D:\\'])
while adf[1] >= 0.05:
    diff = diff + 1
    adf = ADF(data['CWXT_DB:184:D:\\'].diff(diff).dropna())

print(u'原始序列经过%s阶差分后归于平稳，p值为%s' %(diff,adf[1]))