# -*- encoding=utf-# -*-
__author = 'heathu'


##学习numpy库
from numpy import *

print random.rand(4,4)              #打印一个4*4的矩阵
randMat = mat(random.rand(4,4))     #将数组转化成矩阵
print randMat.I                     #求一个矩阵的逆矩阵
invRandMat = randMat.I
print randMat*invRandMat            #矩阵和其逆矩阵的乘积
myEye = randMat*invRandMat
print myEye - eye(4)                #与单位矩阵相减