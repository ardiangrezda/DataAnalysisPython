# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:44:10 2021

@author: msi1
"""
from numpy import array, concatenate, vstack, hstack
x13 = array([
    [4, 5],
    [2, 1]])

x14 = array([
    [15, 16],
    [12, 10]
    ])

print ("x13 = \n", x13)
print ("---------------------------")
print ("x14 = \n", x14)
print ("---------------------------")

x15 = concatenate((x13, x14), axis=0)
print ("x15 = \n", x15)
print ("---------------------------")

x16 = concatenate((x13, x14), axis=1)
print ("x16 = \n", x16)
print ("---------------------------")

x17 = vstack((x13, x14))
print ("x17 = \n", x17)
print ("---------------------------")

x18 = hstack((x13, x14))
print ("x18 = \n", x18)
print ("---------------------------")
