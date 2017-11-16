#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd

file = '../data/predictdata.xls'
data = pd.read_excel(file)

abs_ = (data[u'预测值'] - data[u'实际值']).abs()
mae_ = abs_.mean()
rmase_ = ((abs_**2).mean())**0.5
mape_ = (abs_/data[u'实际值']).mean()

print(u'平均绝对误差为:%0.4f,\n均方差误差为：%0.4f,\n平均绝对百分误差:%0.6f.' %(mae_,rmase_,mape_))