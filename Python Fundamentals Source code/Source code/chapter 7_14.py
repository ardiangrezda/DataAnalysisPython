# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:20:10 2021

@author: msi1
"""

from pandas import *
x55 = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

print ("x55 = \n", x55)
print ("---------------------")
x56 = x55.index.is_unique

print ("x56 = ", x56)
print ("---------------------")

print ("x55['a'] = \n", x55['a'])
print ("---------------------")
