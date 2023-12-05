# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 08:11:58 2021

@author: msi1
"""

from pandas import *
import numpy as np

x19 = Series([3.5, 2.8, -3.9, 1.3], 
             index=['e', 'b', 'a','m'])
print ("x19 = \n", x19)
print ("----------------------------")

x20 = x19.reindex(['a', 'b', 'c', 'd', 'e'])
print ("x20 = \n", x20)
print ("----------------------------")

x21 = Series(['red', 'green', 'blue'],
             index=[0, 2, 4])
x22 = x21.reindex(range(6), method='ffill')

print ("x21 = \n", x21)
print ("----------------------------")
print ("x22 = \n", x22)
print ("----------------------------")

x23 = DataFrame(np.arange(9).reshape((3,3)),
                index = ['a', 'c', 'd'],
                columns = ['Holland', 'France','Spain'])

x24 = x23.reindex(['a', 'b', 'c', 'd'])

print ("x23 = \n", x23)
print ("----------------------------")
print ("x24 = \n", x24)
print ("----------------------------")

states = ['Spain', 'Holland', 'Canada']
x25 = x23.reindex(columns=states)

print ("x23 = \n", x23)
print ("----------------------------")
print ("x25 = \n", x25)
print ("----------------------------")

x26 = x23.reindex(index=['a', 'b', 'c', 'd'])
print ("x23 = \n", x23)
print ("----------------------------")
print ("x26 = \n", x26)
print ("----------------------------")


