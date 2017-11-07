#-*- coding:utf-8 -*-
# Peishichao

import matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs' #定义标签

sizes = [15,30,45,10] #定义每一块的比例
colors = ['yellowgreen','gold','lightskyblue','lightcoral']#定义颜色
explode = (0,0.1,0,0)#定义突出显示
plt.pie(sizes,explode=explode,labels = labels,colors= colors,autopct='%1.1f%%' ,shadow=True,startangle=90)
plt.axis('equal')#显示为圆
plt.show()

import numpy as np
x = np.random.randn(1000)#1000个服从正态分布的随机数
plt.hist(x,10)#分成10组进行绘制
plt.show()


import pandas as pd
D = pd.DataFrame([x,x+1]).T#构造两列的dataFrame
D.plot(kind = 'box')#调用series内置的作图画图
plt.show()