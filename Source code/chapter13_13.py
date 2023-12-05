# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 07:00:47 2022

@author: msi1
"""

import pandas as pd
x52 = pd.date_range('1/1/2020', periods=3, freq='M')

print ("x52 = ", x52)
print ("-------------------------------")

import numpy as np
x53 = pd.Series(np.array([5, 2, 23]), index = x52)
print ("x53 = \n", x53)
print ("-------------------------------")

x54 = x53.to_period()
print ("x54 = \n", x54)
print ("-------------------------------")

x55 = pd.date_range('1/29/2020', periods=4,freq='D')
print ("x55 = ", x55)
print ("-------------------------------")

x56 = pd.Series(np.array([1, 6, 2, 66]), index=x55)
print ("x56 = \n", x56)
print ("-------------------------------")

x57 = x56.to_period('M')
print ("x57 = \n", x57)
print ("-------------------------------")
