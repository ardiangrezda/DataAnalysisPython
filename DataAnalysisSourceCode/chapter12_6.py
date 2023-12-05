# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 06:38:43 2022

@author: msi1
"""

from pandas import *
import numpy as np
x15 = DataFrame(np.array([[1, 3, 5, 7],[2, 4, 6, 8],
                          [-1, -3, -5, -7], [-2, -4, -6 ,8]]),
                columns=['a','b','c', 'd'],
                index=['Joe','Steve', 'Wes','Jim'])
print ("x15 = \n", x15)
print ("------------------------")
x16 = {'a':'red', 'b':'red', 'c':'blue', 'd':'blue', 'f':'orange'}

x17 = x15.groupby(x16, axis=1).sum()
print ("x17 = \n", x17)
print ("------------------------")

x18 = x15.groupby(len).sum()
print ("x18 = \n", x18)
print ("------------------------")

x19 = ['one','one','one', 'two']
x20 = x15.groupby([len, x19]).min()

print ("x20 = \n", x20)
print ("------------------------")
