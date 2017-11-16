#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

discfile = '../data/discdata_processed.xls'
data = pd.read_excel(discfile,index_col='COLLECTTIME')

data = data.iloc[:len(data)-5]
xdata = data['CWXT_DB:184:D:\\']

from statsmodels.tsa.arima_model import ARIMA

pmax = int(len(xdata)/10)
qmax = int(len(xdata)/10)
bic_matrix = []

for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:
            tmp.append(ARIMA(xdata,(p,1,q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
print(bic_matrix)
bic_matrix = pd.DataFrame(bic_matrix)
print(bic_matrix)
print(bic_matrix.stack())
p,q = bic_matrix.stack().idxmin()

print(u'BIC最小的p和q分别是:%s,%s' %(p,q))