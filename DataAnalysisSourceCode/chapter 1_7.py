# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:29:06 2021

@author: msi1
"""

from pandas import *
import numpy as np

x27 = Series(np.arange(5.), index = ['a','b','c','d','e'])
x28 = x27.drop('d')

print ("x27 = \n", x27)
print ("---------------------------")
print ("x28 = \n", x28)
print ("---------------------------")

x29 = x27.drop(['a', 'e'])
print ("x29 = \n", x29)
print ("---------------------------")

x30 = DataFrame(np.arange(16).reshape((4,4)),
            index=['England', 'Canada', 'USA', 'New Zealand'],
            columns=['one', 'two', 'three', 'four'] )
x31 = x30.drop(['Canada', 'USA'])

print ("x30 = \n", x30)
print ("---------------------------")
print ("x31 = \n", x31)
print ("---------------------------")

x32 = x30.drop('two', axis=1)
print ("x32 = \n", x32)
print ("---------------------------")