# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 06:49:36 2021

@author: msi1
"""

from pandas import *

x17 = Series(range(3), index = ['a','b','c'])

x18 = x17.index

print ("x17 = \n", x17)
print ("x18 = ", x18)

x18[1] = 'd'
