#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

catering_sale = '../data/catering_sale_all.xls'
data = pd.read_excel(catering_sale,index_col = u'日期')

print(data.corr())
print(data.corr()[u'百合酱蒸凤爪'])

print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))