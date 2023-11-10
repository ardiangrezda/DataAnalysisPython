# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 07:06:15 2023

@author: msi1
"""

from numpy import *

x4 = [6, 3, 2, 5]
x5 = array(x4)
print ("x4 = ", x4)
print ("x5 = ", x5)
print ("x5.dtype = ", x5.dtype)
print ("----------------------------")

x6 = [6.0, 3, 2, 5]
x7 = array(x6)
print ("x6 = ", x6)
print ("x7 = ", x7)
print ("x7.dtype = ", x7.dtype)
print ("----------------------------")

x8 = [6, 2, 1, 13]
x9 = array(x8)
print ("x8 = ", x8)
print ("x9 = ", x9)
print ("x9.dtype = ", x9.dtype)
print ("----------------------------")

x10 = array(x8, dtype='float64')
print ("x10 = ", x10)
print ("x10.dtype = ", x10.dtype)
print ("----------------------------")