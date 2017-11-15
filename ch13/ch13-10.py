#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
import numpy as np
from GM11 import GM11
inputfile = '../data/data3.csv'
outputfile = '/tmp/data3_GM11.xls'
data = pd.read_csv(inputfile)
data.index = range(1999,2014)

data.iloc[2014] = None
data.iloc[2015] = None

l = ['x3','x4','x6','x8']
for i in l:
    f = GM11(data[i][range(1999,2014)].as_matrix())[0]
    data[i][2104] = f(len(data)-1)
    data[i][2015] = f(len(data))
    data[i] = data[i].round()

data[l+'y'].to_excel(outputfile)