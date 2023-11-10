# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 06:28:45 2021

@author: msi1
"""

from numpy import *
x32 = array([
    [1.2, 1.3, 1.4, 1.5],
    [-1.2, -1.5, -1.8, -2],
    [2.2, 3.1, 2, 1]
    ])

print ("x32 = \n", x32)
print ("----------------------------")

x39 = sort(x32)
print ("x39 = \n", x39)
print ("----------------------------")


x40 = sort(x32, 0)
print ("x40 = \n", x40)
print ("----------------------------")

x41 = array([-1, 3, 2, -4, 7, 4])
print ("x41 = \n", x41)
print ("----------------------------")

x41.sort()
print ("After sort as a method, x41 = \n", x41)
print ("----------------------------")

x41 = array([-1., 3, 2, -4, 7, 4])
x41[1] =nan
print ("After putting nan for an element x41 = \n", x41)
print ("----------------------------")

x42 = sum(x41)
print ("x42 = \n", x42)
print ("----------------------------")

x43 = nansum(x41)
print ("x43 = \n", x43)
print ("----------------------------")

