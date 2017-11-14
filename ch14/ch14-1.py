#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

filename = '../data/business_circle.xls'
standardizedfile = '../tmp/standardized.xls'

data = pd.read_excel(filename,index_col=u'基站编号')
data = (data - data.min())/(data.max()- data.min())

data = data.reset_index()

data.to_excel(standardizedfile,index = False)