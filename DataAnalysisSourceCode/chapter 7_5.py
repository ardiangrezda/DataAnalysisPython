# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 07:21:36 2022

@author: msi1
"""

from datetime import datetime
from pandas import *

x13 = [datetime(2021, 1, 2), datetime(2021, 1, 5),
       datetime(2021, 1, 7), datetime(2021, 1, 8),
       datetime(2021, 1, 10)]

x14 = Series([52, 12, 33, 1, 3], index = x13)

print ("x14 = \n", x14)
print ("-------------------------------")

x15 = x14.index[0]
print ("x15 = \n", x15)
print ("-------------------------------")

x16 = x14.index[2]
print ("x16 = ", x16)
print ("-------------------------------")

x17 = x14[x16]
print ("x17 = ", x17)
print ("-------------------------------")

import numpy as np
import pandas as pd
x18 = Series(np.arange(1000), 
        index = pd.date_range('1/1/2015', periods=1000))
print ("x18 = \n", x18)
print ("-------------------------------")

x19 = x18['2016']
print ("x19 = \n", x19)
print ("-------------------------------")

x20 = x18['2016-05']
print ("x20 = \n", x20)
print ("-------------------------------")

x21 = x14[datetime(2021, 1, 7):]
print ("x14 = \n", x14)
print ("-------------------------------")
print ("x21 = \n", x21)
print ("-------------------------------")

x22 = pd.date_range('1/1/2015', periods=100,freq='W-WED')
print ("x22 = \n", x22)
print ("-------------------------------")

x23 = DataFrame(np.around(np.random.randn(100,4),2),
            index = x22, 
            columns=['Canada','USA','UK', 'France'])
print ("x23 = \n", x23)
print ("-------------------------------")

x24 = x23.loc['2015-05']
print ("x24 = \n", x24)
print ("-------------------------------")

















