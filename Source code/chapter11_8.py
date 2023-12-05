# -*- coding: utf-8 -*-
"""
Created on Sun May  1 07:26:04 2022

@author: msi1
"""

from pandas import *
x41 = DataFrame({'k1':['one']*3 + ['two']*2,
                 'k2':[1, 1, 2, 3, 3]})

print ("x41 = \n", x41)
print ("--------------------------")

x42 = x41.duplicated()
print ("x42 = \n", x42)
print ("--------------------------")

x43 = x41.drop_duplicates()
print ("x43 = \n", x43)
print ("--------------------------")
