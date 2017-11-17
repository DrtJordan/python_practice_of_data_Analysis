#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

threshold = pd.Timedelta(minutes=4)
inputfile = '../data/water_heater.xls'
outputfile = '../tmp/dividsequence.xls'

data = pd.read_excel(inputfile)
data[u'发生时间'] = pd.to_datetime(data[u'发生时间'],format='%Y%m%d%H%M%S')
data = data[data[u'水流量'] > 0]
print(data[u'发生时间'])
print(data[u'发生时间'].diff())
d = data[u'发生时间'].diff() > threshold
print(d.cumsum())
data[u'事件编号'] = d.cumsum() + 1
data.to_excel(outputfile)