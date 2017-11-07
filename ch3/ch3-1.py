#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'日期')#读取数据，指定日期列为索引列

import matplotlib.pyplot as plt#导入图像库

plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号

plt.figure()#建立图像

#p = data.boxplot()
p = data.boxplot(return_type='dict')#画箱线图，直接使用DataFrame的方法

x = p['fliers'][0].get_xdata()#fliers为异常值
y = p['fliers'][0].get_ydata()
y.sort()#从大到小排序


#使用annotate添加注释
for i in range(len(x)):
    if i >0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i] + 0.05 - 0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy = (x[i],y[i]),xytext = (x[i] + 0.08,y[i]))
plt.show()