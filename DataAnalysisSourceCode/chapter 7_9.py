# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 07:53:27 2022

@author: msi1
"""

from pandas.tseries.offsets import Hour, Minute

x35 = Hour()
x36 = Hour(4)

print ("x35 = ", x35)
print ("------------------------")
print ("x36 = ", x36)
print ("------------------------")

import pandas as pd

x37 = pd.date_range('1/1/2000', '1/2/2000 23:59', freq='4h')
print ("x37 = ", x37)
print ("------------------------")
