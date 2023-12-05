# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 07:43:06 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x25 = pd.DatetimeIndex(['1/1/2018', '1/2/2018',
        '1/2/2018', '1/2/2018', '1/3/2018'])
x26 = pd.Series(np.arange(5), index=x25)

print ("x25 = ", x25)
print ("-----------------------------------")
print ("x26 = \n", x26)
print ("-----------------------------------")

x27 = x26.index.is_unique
print ("x27 = ", x27)
print ("-----------------------------------")

x28 = x26['2018-01-02']
print ("x28 = \n", x28)
print ("-----------------------------------")
