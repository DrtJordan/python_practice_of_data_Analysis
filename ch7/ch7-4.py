#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

from sklearn.cluster import KMeans
def job():
    inputfile = '../tmp/zscoreddata.xls'


    k = 5
    data = pd.read_excel(inputfile)

    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data)

    print(kmodel.cluster_centers_)
    print(kmodel.labels_)

if __name__ == "__main__":
    job()