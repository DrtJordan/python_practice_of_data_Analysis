#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd

filename = '../data/bankloan.xls'
data = pd.read_excel(filename)

x = data.iloc[:,:8].as_matrix()

y = data.iloc[:,8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR

from sklearn.linear_model import RandomizedLogisticRegression as RLR

rlr = RLR()

rlr.fit(x,y)

rlr.get_support()
print(rlr.get_support())
print('end')

#print('Feature: %s ' % ','.join(data.columns[rlr.get_support()]))

x = data[data.columns[rlr.get_support()]].as_matrix()
print(x)
lr = LR()
lr.fit(x,y)
print('end')
print('accur: %s' % lr.score(x,y))