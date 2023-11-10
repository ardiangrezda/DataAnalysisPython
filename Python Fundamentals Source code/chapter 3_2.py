# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 06:35:43 2021

@author: msi1
"""

from numpy import array, arange, reshape
x5 = array([[5, 6, 9]])
x6 = array([[0], [1], [2]])
x7 = x5 + x6

print ("x5 = \n", x5)
print ("----------------------------")
print ("x6 = \n", x6)
print ("----------------------------")
print ("x7 = \n", x7)
print ("----------------------------")

x8 = reshape(arange(15), (3, 5))
x9 = 1
x10 = x8 + x9
print ("----------------------------")
print ("x8 = \n", x8)
print ("----------------------------")
print ("x10 = \n", x8)


x11 = arange(3)
x12 = x8 + x11
