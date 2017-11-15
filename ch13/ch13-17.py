#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
inputfile = '../tmp/data5_GM11.xls'
outputfile = '../data/personal_income.xls'
modelfile = '../tp/5-net.model'
data = pd.read_excel(inputfile)
feature = ['x1','x4','x5','x7']

data_train = data.loc[range(2000,2014)].copy()
data_mean = data_train.mean()
data_std = data_train.std()

x_train = data_train[feature].as_matrix()
y_train = data_train['y'].as_matrix()

from keras.models import Sequential
from keras.layers.core import Dense,Activation

model = Sequential()
model.add(Dense(4,8))
model.add(Activation('relu'))
model.add(Dense(8,1))
model.compile(loss = 'mean_squared_error',optimizer='adam')
model.fit(x_train,y_train,nb_epoch=5000,batch_size=16)
model.save_weights(modelfile)


x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix()
data[u'y_pred'] = model.predict(x)*data_std['y'] + data_mean['y']

data[u'y_pred'] = data[u'y_pred'].round()
data.to_excel(outputfile)

import matplotlib.pyplot as plt
p = data[['y',u'y_pred']].plot(subplots = True,style = ['b-o','r-*'])
plt.show()