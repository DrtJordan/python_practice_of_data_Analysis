#-*- coding:utf-8 -*-
# Peishichao

def jobs():
    import numpy as np

    import pandas as pd

    inputfile = '../data/consumption_data.xls'
    k =3
    threshold = 2
    iteration = 500

    data = pd.read_excel(inputfile,index_col = 'Id')

    data_zs = 1.0*(data - data.mean())/data.std()#数据标准化

    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=k,n_jobs=4,max_iter=iteration)
    model.fit(data_zs)#训练数据
    #print(model.labels_)#每个样本对应的类别
    #print(pd.Series(model.labels_,index = data.index))#将类别对应到Id索引上面
    #print(data_zs)#标准化之后的数据

    r = pd.concat([data_zs,pd.Series(model.labels_,index = data.index)],axis=1)
    #print(r)#叠加之后的数据
    #print(list(data.columns))#列表头
    r.columns = list(data.columns) + [u'聚类类别']
    norm = []
    #print(r.columns)
    #print(model.cluster_centers_)
    #print(np.linalg.norm)
    for i in range(k):#逐一的处理
        norm_tmp = r[['R','F','M']][r[u'聚类类别']==i] - model.cluster_centers_[i]
        norm_tmp = norm_tmp.apply(np.linalg.norm,axis = 1)
        #print(norm_tmp)
        norm.append(norm_tmp/norm_tmp.median())
    #print(norm)
    #print('---------------------------')
    norm = pd.concat(norm)#合并
    #print(norm)
    import matplotlib.pyplot as plt

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    norm[norm <= threshold].plot(style = 'go')#正常点
    discreate_points = norm[norm > threshold]
    discreate_points.plot(style = 'ro')

    for i in range(len(discreate_points)):
        id = discreate_points.index[i]

        n = discreate_points.iloc[i]
        print (n)
        plt.annotate('(%s,%0.2f)'%(id,n),xy = (id,n),xytext = (id,n))
    plt.xlabel(u'编号')
    plt.ylabel(u'相对距离')
    plt.show()

if __name__ == '__main__':
    jobs()