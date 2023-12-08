# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 07:25:50 2021

@author: msi1
"""

from pandas import *
import pandas as pd

x9 = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print ("x9 = \n", x9)
print ("-------------------------")

x10 = x9.unique()
print ("x10 = \n", x10)
print ("-------------------------")

x11 = x9.value_counts()
print ("x11 = \n", x11)
print ("-------------------------")

mask = x9.isin(['b','c'])

print ("mask = \n", mask)
print ("-------------------------")

print ("x9[mask] = \n", x9[mask])
print ("-------------------------")

x12 = DataFrame({'Q1': [1, 3, 4, 3, 4],
                 'Q2': [2, 3, 1, 2, 3],
                 'Q3': [1, 5, 2, 4, 4]})
print ("x12 = \n", x12)
print ("-------------------------")

x13 = x12.apply(pd.value_counts).fillna(0)
print ("x13 = \n", x13)
print ("-------------------------")


