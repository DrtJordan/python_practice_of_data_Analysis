#-*- coding:utf-8 -*-
# Peishichao
import numpy as np
from sklearn.decomposition import PCA
D = np.random.rand(10,4)
pca = PCA()
pca.fit(D)
print(pca.components_)
pca = PCA(2)
pca.fit(D)
data = pca.transform(D)
print(data)