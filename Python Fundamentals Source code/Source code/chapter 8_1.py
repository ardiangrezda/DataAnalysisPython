# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:10:37 2021

@author: msi1
"""

from pandas import *
import numpy as np
x1 = DataFrame([[6.4, np.nan], [4.9, -2.5],
                [np.nan, np.nan], [0.5, -1.9]],
               index = ['a','b','c','d'],
               columns = ['one', 'two'])

print ("x1 = \n", x1)
print ("-----------------------")

x2 = x1.sum()
print ("x2 = \n", x2)
print ("-----------------------")

x3 = x1.sum(axis=1)
print ("x3 = \n", x3)
print ("-----------------------")

x4 = x1.idxmax()
print ("x4 = \n", x4)
print ("-----------------------")

x5 = x1.cumsum()
print ("x5 = \n", x5)
print ("-----------------------")

x6 = x1.describe()
print ("x6 = \n", x6)
print ("-----------------------")

x7 = Series(['a', 'c', 'b', 'a'] * 3)
print ("x7 = \n", x7)
print ("-----------------------")

x8 = x7.describe()
print ("x8 = \n", x8)
print ("-----------------------")

