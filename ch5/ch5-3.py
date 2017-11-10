#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

inputfile = '../data/sales_data.xls'

data = pd.read_excel(inputfile,index_col=u'序号')

data[data == u'好'] = 1
data[data == u'高'] = 1
data[data == u'是'] = 1

data[data !=1 ] = 0

x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

from keras.models import Sequential

from keras.layers.core import Dense, Activation

model = Sequential()#建立模型
model.add(Dense(input_dim=3, units=10))
model.add(Activation('relu'))#激活函数
model.add(Dense(input_dim=10, units=1))
model.add(Activation('sigmoid'))

model.compile(loss = 'binary_crossentropy',optimizer='adam')
model.fit(x,y,epochs=1000,batch_size = 10)

yp = model.predict_classes(x).reshape(len(y))

#from cm_plot import *

#cm_plot(y,yp).show()
print (y)
print (yp)