#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd
import numpy as np
datafile = '../data/normalization_data.xls'

data = pd.read_excel(datafile,header=None)

print((data - data.min())/(data.max() - data.min()))#最小最大规范化
print((data - data.mean())/data.std())#零- 均值规范化
print(data/10**np.ceil(np.log10(data.abs().max())))#小数定标规范化