#-*- coding:utf-8 -*-
# Peishichao
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000) #自变量
y = np.sin(x) + 1#因变量
z = np.cos(x**2) + 1#因变量

plt.figure(figsize=(8, 4)) #图像大小
plt.plot(x, y, label='$\sin x + 1$', color='red', linewidth=2)#设置标签、线条颜色、线条大小

'''
中文字体
'''
plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示中文标签
'''
负号显示不正确
'''
plt.rcParams['axes.unicode_minus'] = False#解决保存图像是负号'-'显示方块的问题

plt.plot(x, z, 'b--', label='$\cos x^2 + 1$')#线条类型
plt.xlabel('Time(s) ')
plt.ylabel('Volt')
plt.title('A simple Example')
plt.ylim(0, 2.2)#y轴范围
plt.legend()#显示图例
plt.show()#显示作图结果
