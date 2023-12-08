# -*- coding: utf-8 -*-
"""
Created on Tue May 24 07:22:06 2022

@author: msi1
"""

from pandas import *

x1 = DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':[0.2, 0.25, 0.3, 0.35, 0.4],
                'data2':[1.4, 1.45,1.5, 1.55, 1.6]})

print ("x1 = \n", x1)
print ("---------------------------")

x2 = x1['data1'].groupby(x1['key1'])
x3 = x2.mean()

print ("x2 = \n", x2)
print ("---------------------------")
print ("x3 = \n", x3)
print ("---------------------------")

x4 = x1['data1'].groupby([x1['key1'], x1['key2']]).mean()
print ("x4 = \n", x4)
print ("---------------------------")

x5 = x4.unstack()
print ("x5 = \n", x5)
print ("---------------------------")

import numpy as np
x6 = np.array(['UK','USA', 'USA', 'UK','USA'])
x7 = np.array([2015, 2015, 2016, 2015, 2016])

x8 = x1['data1'].groupby([x6, x7]).mean()
print ("x8 = \n", x8)
print ("---------------------------")

x9 = x1.groupby('key1').mean()
print ("x9 = \n", x9)
print ("---------------------------")
