# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 08:09:28 2022

@author: msi1
"""

from pandas import *

x33 = DataFrame({'a':range(5), 'b': range(5, 0, -1),
                 'c': ['one', 'one','two','two','two'],
                 'd':[0, 1, 0, 1, 2]})
print ("x33 = \n", x33)
print ("----------------------------")

x34 = x33.set_index(['c','d'])
print ("x34 = \n", x34)
print ("----------------------------")

x35 = x34.reset_index()
print ("x35 = \n", x35)
print ("----------------------------")
