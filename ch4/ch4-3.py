#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

datafile = '../data/discretization_data.xls'
data = pd.read_excel(datafile)

data = data[u'肝气郁结证型系数'].copy()

k = 4
d1 = pd.cut(data,k,labels =range(k))
#等宽离散化，各个类以此命名为0,1,2,3

#等频率离散化
w= [1.0*i/k for i in range(k+1)]
#使用describe自动计算分位数
w = data.describe(percentiles = w)[4:4+k+1]
w[0] = w[0]*(1-1e-10)

d2 = pd.cut(data, w, labels=range(k))

from sklearn.cluster import KMeans

kmodel = KMeans(n_clusters=k,n_jobs=4)#建立模型
kmodel.fit(data.reshape((len(data),1)))#训练数据
c = pd.DataFrame(kmodel.cluster_centers_).sort(0)#输出聚类中心点，并且排序

w = pd.rolling_mean(c,2).iloc[1:]#相邻两项求中点，作为边界点

w = [0] + list(w[0]) + [data.max()]#把首末边界点加上

d3 = pd.cut(data, w, labels=range(k))

def cluster_polt(d,k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8,3))
    for j in range(0,k):
        plt.plot(data[d==j],[j for i in d[d==j]],'o')
    plt.ylim(-0.5,k-0.5)
    return plt

cluster_polt(d1,k).show()
cluster_polt(d2,k).show()
cluster_polt(d3,k).show()

