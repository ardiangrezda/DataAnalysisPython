# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:06:15 2021

@author: msi1
"""

from pandas import *
import numpy as np

x46 = Series(range(4), index=['d', 'a', 'b','c'])
print ("x46 = \n", x46)
print ("----------------------------")

x47 = x46.sort_index()
print ("x47 = \n", x47)
print ("----------------------------")


x48 = DataFrame(np.arange(12).reshape((3,4)),
            index=['three', 'one', 'four'],
            columns = ['d', 'a', 'b', 'c'])
print ("x48 = \n", x48)
print ("----------------------------")

x49 = x48.sort_index()
print ("x49 = \n", x49)
print ("----------------------------")

x50 = x48.sort_index(axis=1)
print ("x50 = \n", x50)
print ("----------------------------")

x51 = Series(array([7, -2, 10, 3]), index=['d','a','b','c'])
print ("x51 = \n", x51)
print ("----------------------------")

x52 = x51.sort_values()
print ("x52 = \n", x52)
print ("----------------------------")

x53 = DataFrame(np.array([[1, 6, 2], [2, 7, 10], 
                [0, 1, 4]]), index=['one','two', 'three'],
                columns =['a', 'b', 'c'])
print ("x53 = \n", x53)
print ("----------------------------")

x54 = x53.sort_values(by=['b'])
print ("x54 = \n", x54)
print ("----------------------------")



