# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 07:50:30 2021

@author: msi1
"""

from pandas import *
from numpy import linspace, nan

x22 = DataFrame(linspace(10, 17, 21).reshape((7,3)))
x22.loc[:4,1] = nan; x22.loc[:2, 2] = nan
print ("x22 = \n", x22)
print ("-------------------------------")

x23 = x22.fillna(0)
print ("x23 = \n", x23)
print ("-------------------------------")

x24 = x22.fillna({1:0.5, 4:3})
print ("x24 = \n", x24)
print ("-------------------------------")

x25 = Series([1.3, nan, 9.5, nan, 5])
x26 = x25.fillna(x25.mean())

print ("x25 = \n", x25)
print ("-------------------------------")
print ("x26 = \n", x26)
print ("-------------------------------")
