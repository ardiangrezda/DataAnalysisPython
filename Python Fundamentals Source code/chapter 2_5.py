# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 07:03:15 2021

@author: msi1
"""
from numpy import array
x19 = array([7, 4, 3, 9, 11])

print ("x19 = ", x19)
print ("x19[0] = ", x19[0])

print ("-----------------------------------")
x20 = array([
    [1, 6, 3],
    [9, 15, 4]
    ])
print ("x20 = \n", x20)
print ("x20[1, 2] = ", x20[1, 2])

print ("-----------------------------------")

x21 = array([9, 7, 4, 2, 1])
print ("Before x21 = \n", x21)
x21[0] = -7 
print ("After x21 = \n", x21)
print ("-----------------------------------")