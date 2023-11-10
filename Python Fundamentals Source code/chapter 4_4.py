# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 06:51:48 2021

@author: msi1
"""

from numpy import *
x14 = zeros((5, 5))

for i in range(size(x14, 0)):
    if (i % 2) == 1:
        for j in range(size(x14, 1)):
            x14[i, j] = i + j + 10
    else:
        for j in range(int(i/2)):
            x14[i, j] = i - j - 20

print ("x14 = \n", x14)
print ("-----------------------")


x15 = linspace(0, 10, 6)
for i,j in enumerate(x15):
    print ("i = ", i, " j = ", j)
