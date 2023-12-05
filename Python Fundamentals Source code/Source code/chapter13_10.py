# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:38:34 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x38 = pd.Series(np.array([55, 22, 33, 44]),
    index = pd.date_range('1/1/2020', periods=4, freq='M'))

print ("x38 = \n", x38 )
print ("--------------------------")

x39 = x38.shift(3, freq='D')
print ("x39 = \n", x39 )
print ("--------------------------")

x40 = x38.shift(1, freq='90T')
print ("x40 = \n", x40 )
print ("--------------------------")
