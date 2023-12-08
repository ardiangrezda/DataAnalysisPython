# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 07:36:08 2021

@author: msi1
"""

from pandas import *
import numpy as np

x33 = Series(np.arange(4.)+3 , index = ['a','b','c','d'])

print ("x33 = \n", x33)
print ("---------------------")

print ("x33['c'] = ", x33['c'])
print ("---------------------")

print ("x33[2] = ", x33[2])
print ("---------------------")

print ("x33[2:4] = \n", x33[2:4])
print ("---------------------")

print ("x33[['b', 'c', 'a']] = \n", x33[['b', 'c', 'a']])
print ("---------------------")

print ("x33[[1, 3]] =  \n", x33[[1, 3]])
print ("---------------------")

print ("x33[x33 < 5] = \n", x33[x33 < 5])
print ("---------------------")

x33['b':'c'] = 15

print ("After updating, x33 = \n", x33)
print ("---------------------")

x34 = DataFrame((np.arange(16) + 0.3).reshape((4,4)),
            index= ['USA','Canada','Mexico','Panama'],
            columns = ['one', 'two', 'three', 'four'])
print ("x34 = \n", x34)
print ("---------------------")

print ("x34['two'] = \n", x34['two'])
print ("---------------------")

print ("x34[['three','one']] = \n", x34[['three','one']])
print ("---------------------")

print ("x34[:2] = \n", x34[:2])
print ("---------------------")

x35 = x34[x34['three'] > 7]
print ("x35 = \n ", x35)
print ("---------------------")

x34[x34<5 ] = -10
print ("After modifying, x34 = \n ", x34)
print ("---------------------")

print ("x34.loc['Mexico', ['two','three']] = \n", 
       x34.loc['Mexico', ['two','three']])
print ("---------------------")

print ("x34.iloc[2] = \n", x34.iloc[2])
print ("---------------------")

print ("x34.loc[['Canada', 'USA'], ['three', 'two']] = \n", 
       x34.loc[['Canada', 'USA'], ['three', 'two']])
print ("---------------------")

print ("x34.loc['Panama'] = \n", x34.loc['Panama'])
print ("---------------------")
