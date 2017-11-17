#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd
datafile = '../data/air_data.csv'
resultfile = '../tmp/explore.xls'

data = pd.read_csv(datafile,encoding='utf-8')

explore = data.describe(percentiles=[],include='all').T

explore['null'] = len(data) - explore['count']
explore = explore[['null','max','min']]
explore.columns = [u'空值数',u'最大值',u'最小值']
explore.to_excel(resultfile)
