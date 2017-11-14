#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

import jieba

inputfile1 = '../data/meidi_jd_neg.txt'
inputfile2 = '../data/meidi_jd_pos.txt'
outputfile1 = '../data/meidi_jd_neg_cut.txt'
outputfile2 = '../data/meidi_jd_pos_cut.txt'

data1 = pd.read_csv(inputfile1,encoding='utf-8',header=None)
data2 = pd.read_csv(inputfile2,encoding='utf-8',header=None)

mycut = lambda s : ' '.join(jieba.cut(s))
print(data1)
print(data1[0])
data1 = data1[0].apply(mycut)
data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1,index=False,header = False)
data2.to_csv(outputfile2,index=False,header = False)