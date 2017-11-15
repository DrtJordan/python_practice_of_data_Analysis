#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
inputfile = '../tmp/data1_GM11.xls'
outputfile = '../data/revenue.xls'
modelfile = '../tmp/1-net.model'
data = pd.read_excel(inputfile)

feature = ['x1','x2','x3','x4','x5','x7']#特征所在的列

data_train = data.loc[range(1994,2014)].copy()#取2014年券的数据进行建模
data_mean = data_train.mean()
data_std = data_train.std()

data_train = (data_train - data_mean)/data_std#数据标准化

x_train = data_train[feature].as_matrix()#特征数据

y_train = data_train['y'].as_matrix()#标签数据

from keras.models import Sequential
from keras.layers.core import Dense,Activation

model = Sequential()#建立模型
model.add(Dense(6,12))
model.add(Activation('relu'))
model.add(Dense(12,1))
model.compile(loss = 'mean_squared_error',optimizer='adam')#编译模式
model.fit(x_train,y_train,nb_epoch=1000,batch_size=16)#训练模型
model.save_weights(modelfile)#保存结果参数

x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix()
data[u'y_pred'] = model.predict(x)*data_std['y'] + data_mean['y']
data.to_excel(outputfile)

import matplotlib.pyplot as plt
p = data[['y',u'y_pred']].plot(subplots = True, style = ['b-o','r-*'])
plt.show()