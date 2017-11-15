#-*- coding:utf-8 -*-
# Peishichao

import numpy as np
import pandas as pd

inputfile = '../data/data1.csv'
data = pd.read_csv(inputfile)
r = [data.min(),data.max(),data.mean(),data.std()]

r = pd.DataFrame(r,index = ['Min','Max','Mean','STD']).T
np.round(r,2)

