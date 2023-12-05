# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:00:45 2022

@author: msi1
"""

import pandas as pd
x41 = pd.Period(2020, freq='A-DEC')
print ("x41 = ", x41)
print ("-----------------------------")

x42 = x41 + 5
print ("x42 = ", x42)
print ("-----------------------------")

x43 = x41 - 3
print ("x43 = ", x43)
print ("-----------------------------")


x44 = pd.period_range('1/1/2020', '5/31/2020', freq='M')
print ("x44 = ", x44)
print ("-----------------------------")

import numpy as np

x45 = pd.Series(np.array([11, 33, 12, 31, 4]), index=x44)

print ("x45 = \n", x45)
print ("-----------------------------")

x46 = ['2020Q3', '2021Q2', '2023Q1']
x47 = pd.PeriodIndex(x46, freq='Q-DEC')

print ("x47 = ", x47)
print ("-----------------------------")
