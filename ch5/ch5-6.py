#-*- coding:utf-8 -*-
# Peishichao
import   pandas as pd
from apriori import find_rule
inputfile = '../data/menu_orders.xls'
outputfile = '../data/apriori_rules.xls'

data = pd.read_excel(inputfile,index_col=None)

print(u'\n转化原始数据至0-1矩阵...')

ct  = lambda x : pd.Series(1, index = x[pd.notnull(x)]) #转化0-1矩阵的过度函数

b = map(ct, data.as_matrix())
data = pd.DataFrame(list(b)).fillna(0)

print(u'\n转化完毕')

del b

support = 0.2
confidence = 0.5

ms ='---'
find_rule(data,support,confidence,ms).to_excel(outputfile)