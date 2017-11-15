#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
import numpy as np
from GM11 import GM11
inputfile = '../data/data4.csv'
outputfile = '../tmp/data4_Gm11.xls'

data = pd.read_csv(inputfile)
data.index = range(2002,2014)

data.loc[2014] = None
data.loc[2015] = None

l = ['x1','x2','x3','x4','x6','x7','x9','x10']

for i in l:
    f = GM11(data[i][range(1999,2014)].as_matrix())[0]
    data[i][2014] = f(len(data)-1)
    data[i][2015] = f(len(data))
    data[i] = data[i].round(2)

data[l +'y'].to_excel(outputfile)