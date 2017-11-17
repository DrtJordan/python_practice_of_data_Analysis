#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

from random import shuffle

datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p =0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from keras.models import Sequential
from keras.layers.core import Dense,Activation

netfile = '../tmp/net.model'

net = Sequential()
net.add(Dense(3,10))
net.add(Activation('relu'))
net.add(Dense(10,1))
net.add(Activation('sigmoid'))

net.compile(loss = 'binary_crossentropy',optimizer='adam',class_mode = 'binary')
net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_size=1)

predict_result = net.predict_classes(train[:,:3].reshape(len(train)))

from cm_plot import *
cm_plot(train[:,3],predict_result).show()

from sklearn.tree import DecisionTreeClassifier

treefile = '../tmp/tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])

from sklearn.externals import joblib
joblib.dump(tree,treefile)

from cm_plot import *
cm_plot(train[:,3],tree.predict(train[:,:3])).show()

from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
predict_result  =tree.predict(test[:,:3]).reshape(len(test))
fpr,tpr,thresholds = roc_curve(test[:,3],predict_result,pos_label=1)
plt.plot(fpr,tpr,linewidth =2,lable = 'ROC OF LM')
plt.xlabel('False Posittive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0.1,0.5)
plt.ylim(0.1,0.5)
plt.legend(loc = 4)
plt.show()


predict_result  =net.predict(test[:,:3]).reshape(len(test))
fpr,tpr,thresholds = roc_curve(test[:,3],predict_result,pos_label=1)
plt.plot(fpr,tpr,linewidth =2,lable = 'ROC OF LM')
plt.xlabel('False Posittive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0.1,0.5)
plt.ylim(0.1,0.5)
plt.legend(loc = 4)
plt.show()