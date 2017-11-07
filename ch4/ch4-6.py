#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xls'

data = pd.read_excel(inputfile,header=None)

from sklearn.decomposition import PCA

pca = PCA(3)
pca.fit(data)
print(pca.components_)#返回模型的各个特征向量
print(pca.explained_variance_ratio_)#返回各个成分各自的方差百分比

low_d = pca.transform(data)#降低维度
print(low_d)
pd.DataFrame(low_d).to_excel(outputfile)

pca.inverse_transform(low_d)#复原数据
