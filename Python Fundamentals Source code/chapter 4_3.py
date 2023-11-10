# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 08:01:58 2021

@author: msi1
"""

from numpy import *
from numpy.random import *

x11 = randn(43)
x12 = 0
for i in range(len(x11)):
    if x11[i] < 0:
        x12 += 1
print ("x12 = ", x12)
print ("--------------------------")

x13 = zeros((6, 6))

for i in range(size(x13, 0)):
    for j in range(size(x13, 1)) :
        if i < j: 
            x13[i, j] = i + j + 10
        elif i > j:
            x13[i, j] = i - j - 20
        else:
            x13[i, j] = 99

print ("x13 = \n", x13)
print ("--------------------------")
