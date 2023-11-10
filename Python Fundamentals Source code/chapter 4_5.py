# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 06:42:33 2021

@author: msi1
"""

from numpy.random import *
x16 = randn(1000)

for i in x16:
    print (i)
    if i > 1.2 :
        break

print ("The last value of i is : ", i)
