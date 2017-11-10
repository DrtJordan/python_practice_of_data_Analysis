#-*- coding:utf-8 -*-
# Peishichao

from sklearn.manifold import TSNE
import pandas as pd
inputfile = '../data/consumption_data.xls'
outputfile = '../tmp/data_type.xls'
tsne = TSNE()
data = pd.read_excel(inputfile,index_col='Id')
data_zs = 1.0*(data-data.mean())/data.std()
tsne.fit_transform(data_zs)
tsne = pd.DataFrame(tsne.embedding_,index = data_zs.index)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sklearn.cluster import KMeans
k =3
iteration = 500
model = KMeans(n_clusters=k, n_jobs=1, max_iter=iteration)
model.fit(data_zs)
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类的中心

r = pd.concat([r2, r1], axis=1)  # 横向连接，得到聚类中心对应的类别下得数目

r.columns = list(data.columns) + [u'类别数目']  # 重命名表头

print(r)

r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0],d[1],'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0],d[1],'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0],d[1],'b*')
plt.show()