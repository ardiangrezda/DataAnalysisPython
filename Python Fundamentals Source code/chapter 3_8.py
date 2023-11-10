# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 06:48:57 2021

@author: msi1
"""
from numpy import *
x32 = array([
    [1.2, 1.3, 1.4, 1.5],
    [-1.2, -1.5, -1.8, -2],
    [2.2, 3.1, 2, 1]
    ])
x33 = sum(x32)

print ("x32 = \n", x32)
print ("-----------------------------")
print ("x33 = \n", x33)

x34 = sum(x32, 0)
print ("-----------------------------")
print ("x34 = \n", x34)

x35 = sum(x32, 1)
print ("-----------------------------")
print ("x35 = \n", x35)

x36 = cumsum(x32, 0)
print ("-----------------------------")
print ("x36 = \n", x36)
