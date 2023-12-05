# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 07:26:56 2021

@author: msi1
"""

from pandas import *
import numpy as np

x36 = Series([7.1, -2.5, 2.4, 3.5], index = ['a','c','d','e'])

print ("x36 = \n", x36)
print ("----------------------")

x37 = Series([-5.1, 3.2, -1.5, 4, 3.1], 
             index=['a','c','e','f','g'])
print ("x37 = \n", x37)
print ("----------------------")


x38 = x36 + x37
print ("x38 = \n", x38)
print ("----------------------")

x39 = DataFrame(np.arange(9.).reshape((3,3)), 
                columns = list('bcd'),
                index=['USA', 'Canada','Panama']) 
print ("x39 = \n", x39)
print ("----------------------")


x40 = DataFrame(np.arange(12.).reshape((4,3)), 
                columns = list('bde'),
                index=['Panama','USA', 'Canada','Mexico']) 
print ("x40 = \n", x40)
print ("----------------------")

x41 = x39 + x40
print ("x41 = \n", x41)
print ("----------------------")