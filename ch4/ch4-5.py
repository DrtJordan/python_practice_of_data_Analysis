#-*- coding:utf-8 -*-
# Peishichao

#参数初始化
inputfile = '../data/leleccum.mat'

from scipy.io import loadmat
#mat是python的专用格式，需要用loadmat读取它


mat = loadmat(inputfile)
signal = mat['leleccum'][0]

import pywt
coeffs = pywt.wavedec(signal,'bior3.7',level = 5)

print(coeffs)