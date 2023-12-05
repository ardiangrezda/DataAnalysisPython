# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 06:53:56 2021

@author: msi1
"""

from pandas import *
from numpy import nan as NA

x14 = Series([1.4, NA, 2.3, NA, 7])
print ("x14 = \n", x14)
print ("------------------------")

x15 = x14.dropna()
print ("x15 = \n", x15)
print ("------------------------")
