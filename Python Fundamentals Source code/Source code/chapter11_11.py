# -*- coding: utf-8 -*-
"""
Created on Wed May 11 06:54:56 2022

@author: msi1
"""

from pandas import *
import numpy as np

x49 = DataFrame(np.arange(12).reshape((3,4)),
            index=['Ohio','Colorado','New York'],
            columns=['one','two','three','four'])

print ("x49 = \n", x49)
print ("----------------------------")

x50 = x49.index.map(str.upper)
print ("x50 = \n", x50)
print ("----------------------------")

x49.index = x49.index.map(str.upper)
print ("After index update, x49 = \n", x49)
print ("----------------------------")

x51 = x49.rename(index=str.title,columns=str.upper)

print ("x51 = \n", x51)
print ("----------------------------")


x52 = x49.rename(index={'OHIO':'INDIANA'},
        columns={'three':'pekaboo'})
print ("x52 = \n", x52)
print ("----------------------------")
