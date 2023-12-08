# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 07:33:47 2021

@author: msi1
"""

from pandas import *
import numpy as np

x16 = Series(['apple', 'pear', np.nan, 'banana'])
print ("x16 = \n", x16)
print ("-------------------------")

x17 = x16.isnull()
print ("x17 = \n", x17)
print ("-------------------------")

x18 = DataFrame([[1., 6.5, 3.],
                 [1, np.nan, np.nan],
                 [np.nan, np.nan, np.nan],
                 [np.nan, 6.5, 3.]])

print ("x18= \n", x18)
print ("-------------------------")

x19 = x18.dropna()
print ("x19 = \n", x19)
print ("-------------------------")

x20 = x18.dropna(how='all')
print ("x20= \n", x20)
print ("-------------------------")

x18[4] = np.nan
print ("After adding nan column, x18= \n", x18)
print ("-------------------------")

x21 = x18.dropna(axis=1, how='all' )
print ("x21= \n", x21)
print ("-------------------------")
