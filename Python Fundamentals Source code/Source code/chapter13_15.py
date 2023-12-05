# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 07:58:23 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x60 = pd.date_range('1/1/2020', periods=100,
                    freq='D')
x61 = pd.Series(np.arange(100), index=x60)

print ("x61 = \n", x61)
print ("------------------------------")

x62 = x61.resample('M').mean()
print ("x62 = \n", x62)
print ("------------------------------")

x63 = x61.resample('M',kind='period').mean()
print ("x63 = \n", x63)
print ("------------------------------")

x64 = pd.date_range('1/1/2020', periods=12,
                    freq='T')
x65 = pd.Series(np.arange(12), index=x64)
print ("x65 = \n", x65)
print ("------------------------------")

x66 = x65.resample('5min').sum()
print ("x66 = \n", x66)
print ("------------------------------")

x67 = x65.resample('5min', closed='left').sum()
print ("x67 = \n", x67)
print ("------------------------------")

x68 = x65.resample('5min', closed='right').sum()
print ("x68 = \n", x68)
print ("------------------------------")







