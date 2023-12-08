# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 06:08:37 2022

@author: msi1
"""

import pandas as pd

x48 = pd.period_range('2016','2019', freq='A-DEC')
print ("x48 = ", x48)
print ("-------------------------------")

import numpy as np
x49 = pd.Series(np.array([1, 6, 3, 5]), index=x48)
print ("x49 = \n", x49)
print ("-------------------------------")

x50 = x49.asfreq('M', how='start')
print ("x50 = \n", x50)
print ("-------------------------------")

x51 = x49.asfreq('M', how='end')
print ("x51 = \n", x51)
print ("-------------------------------")