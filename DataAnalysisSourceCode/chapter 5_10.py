# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:20:03 2022

@author: msi1
"""

from pandas import *
import numpy as np
x45 = Series([1., -977, 2, -977, -1044, 9])
print ("x45 = \n", x45)
print ("------------------------------")

x46 = x45.replace(-977, np.nan)
print ("x46 = \n", x46)
print ("------------------------------")

x47 = x45.replace([-977,-1044], np.nan)
print ("x47 = \n", x47)
print ("------------------------------")

x48 = x45.replace({-977:np.nan, -1044:0})
print ("x48 = \n", x48)
print ("------------------------------")
