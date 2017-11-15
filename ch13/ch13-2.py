#-*- coding:utf-8 -*-
# Peishichao

import numpy as np
import pandas as pd

inputfile = '../data/data1.csv'
data = pd.read_csv(inputfile)
np.round(data.corr(method='person'),2)