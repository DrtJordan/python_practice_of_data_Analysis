#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
standardizedfile = '../data/standardized.xls'
k = 3
data = pd.read_excel(standardizedfile,index_col = u'基站编号')

from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=k,linkage='ward')
model.fit(data)

r = pd.concat([data,pd.Series(model.labels_,index = data.index)],axis=1)

r.columns  = list(data.columns) + [u'聚类类别']

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

style = ['ro-','go-','bo-']

xlabels = [u'工作日人均停留时间',u'凌晨人均停留时间',u'周末人均停留时间',u'日均人流量']

pic_output = '../tmp/type_'

for i in range(k):

    plt.figure()
    tmp = r[r[u'聚类类别']== i].iloc[:,:4]
    for j in range(len(tmp)):
        plt.plot(range(1,5),tmp.iloc[j],style[i])

    plt.xticks(range(1,5),xlabels,rotation = 20)
    plt.subplots_adjust(bottom = 0.15)
    plt.savefig(u'%s%s.png' %(pic_output,i))