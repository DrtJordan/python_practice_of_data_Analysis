#-*- coding:utf-8 -*-
# Peishichao

import numpy as np
import pandas as pd
inputfile = '../data/water_heater.xls'
n = 4

threshold = pd.Timedelta(minutes = 5)
data = pd.read_excel(inputfile)

data[u'发生时间'] = pd.to_datetime(data[u'发生时间'],format='%Y%m%d%H%M%S')
data = data[data[u'水流量'] > 0]

def event_num(ts):
    d = data[u'发生时间'].diff() > ts
    return d.sum() + 1

dt = [pd.Timedelta(minutes=i) for i in np.arange(1,9,0.25)]
h = pd.DataFrame(dt,columns=[u'阈值'])
h[u'事件数'] = h[u'阈值'].apply(event_num)
h[u'斜率'] = h['事件数'].diff()/0.25

h[u'斜率指标'] = pd.rolling_mean(h[u'斜率'].abs(),n)
ts = h[u'阈值'][h[u'斜率指标'].idxmin() - n]
if ts > threshold:
    ts = pd.Timedelta(minutes=4)
print(ts)