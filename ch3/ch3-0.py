#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd
catering_sale = '../data/train.csv'

data = pd.read_csv(catering_sale)

print(data.describe())