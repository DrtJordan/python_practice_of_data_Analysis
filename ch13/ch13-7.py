#-*- coding:utf-8 -*-
# Peishichao

import numpy as np

import pandas as pd
from GM11 import GM11

inputfile = '../data/data2.csv'
outputfile = '../tmp/data2_GM11.xls'
data = pd.read_csv(inputfile)
data.index = range(1999,2014)

data.loc[2014] = None
data.loc[2015] = None
l = ['x1','x3','x5']
for i in l:
    f = GM11(data[i][range(1999,2014)].as_matrix())[0]
    print(f)
    data[i][2014] = f(len(data)-1)
    data[i][2015] = f(len(data))
    data[i] = data[i].round(6)

#data[1+['y']].to_excel(outputfile)