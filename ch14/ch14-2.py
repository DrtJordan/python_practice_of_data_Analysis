#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

standardizedfile = '../data/standardized.xls'
data = pd.read_excel(standardizedfile,index_col=u'基站编号')

import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import linkage,dendrogram

z = linkage(data, method = 'ward', metric= 'euclidean')

p = dendrogram(z,0)

plt.show()