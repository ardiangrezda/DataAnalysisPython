# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 07:03:32 2021

@author: msi1
"""

from pandas import Series, DataFrame
import pandas as pd

x1 = Series([4, 9, -2, 11])
print ("x1 = \n", x1)

print ("x1.values = ", x1.values)

print ("x1.index = ", x1.index)

x2 = Series([4, 9, -2, 11], index=['d', 'a', 'k', 'e'])

print ("x2 = \n", x2)
print ("x2['a'] = ", x2['a'])

x2['d'] = 6
print ("x2[['k', 'a', 'd']] = ")
print (x2[['k', 'a', 'd']])

x3 = x2[x2 > 0]
print ("x3 = \n", x3)

x4 = x2 * 2
print ("x2 = \n", x2)
print ("x4 = \n", x4)

x5 = {'England':1300, 'France': 1500, 'Spain': 1800, 'Turkey':1200}
x6 = ['France', 'Spain', 'Germany', 'England']
x7 = Series(x5, index = x6)
print ("x7 = \n", x7)

x8 = pd.isnull(x7)
print ("x8 = \n", x8)

x9 = Series(x5)
print ("x9 = \n ", x9)

x10 = x7 + x9
print ("x10 = \n ", x10)

x7.name = 'statistics'
x7.index.name = 'state'
print ("After putting name atribute, x7 = \n", x7)

x1.index = ['Bill', 'Jim', 'James', 'Kyle']
print ("After putting index, x1 = \n", x1)
