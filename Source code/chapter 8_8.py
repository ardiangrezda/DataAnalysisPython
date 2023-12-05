# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 07:25:31 2021

@author: msi1
"""
from numpy import *
from pandas import *
x27 = Series(linspace(2, 11, 10), 
             index = [['a','a','a','b','b','b','c','c', 'd','d'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print ("x27 = \n", x27)
print ("--------------------------")
print ("x27.index = ", x27.index)
print ("--------------------------")

print ("x27[b] =  \n", x27['b'])
print ("--------------------------")

print ("x27['b':'c''] =  \n", x27['b':'c'])
print ("--------------------------")

print ("x27.loc[['b', 'c']] = \n", x27.loc[['b', 'c']])
print ("--------------------------")

print ("x27[:, 2] = \n", x27[:, 2] )
print ("--------------------------")

x28 = x27.unstack()
print ("x27 = \n", x27)
print ("--------------------------")
print ("x28 = \n", x28)
print ("--------------------------")

x29 = DataFrame(arange(12).reshape((4, 3)),
                index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                columns=[['England', 'England', 'USA'],
                         ['Green', 'Blue', 'Green']])
print ("x29 = \n", x29)
print ("--------------------------")

x29.index.names=['key1', 'key2']
x29.columns.names=['state', 'color']
print ("After modifying index and column names, x29 = \n", x29)
print ("--------------------------")

x30 = x29.swaplevel('key1', 'key2')
print ("x30 = \n", x30)
print ("--------------------------")

x31 = x29.sum(level='key2')
print ("x31 = \n", x31)
print ("--------------------------")

x32 = x29.sum(level='color', axis=1)
print ("x32 = \n", x32)
print ("--------------------------")

