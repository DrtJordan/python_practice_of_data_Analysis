#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

inputfile = '../data/moment.csv'
data = pd.read_csv(inputfile,encoding='gbk')
data = data.as_matrix()
outputfile = '../tmp/model1.xls'
outputfile2 = '../tmp/model2.xls'
from random import shuffle
shuffle(data)
data_train = data[:int(0.8*len(data)),:]
data_test = data[int(0.2*len(data)):,:]

x_train = data_train[:,2:]*30
y_train = data_train[:,0].astype(int)
x_test = data_test[:,2:]*30
y_test = data_test[:,0].astype(int)

from sklearn import svm
model = svm.SVC()
model.fit(x_train,y_train)
import pickle
pickle.dump(model,open('../tmp/svm.model','wb'))
model = pickle.load(open('../tmp/svm.model','rb'))
from sklearn import metrics
cm_train = metrics.confusion_matrix(y_train,model.predict(x_train))
cm_test = metrics.confusion_matrix(y_test,model.predcit(x_test))

pd.DataFrame(cm_train,index = range(1,6),columns=range(1,6).to_excel(outputfile))
pd.DataFrame(cm_test,index = range(1,6),columns=range(1,6).to_excel(outputfile2))