# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 07:09:06 2022

@author: msi1
"""

from datetime import datetime
from pandas import *

x13 = [datetime(2021, 1, 2), datetime(2021, 1, 5),
       datetime(2021, 1, 7), datetime(2021, 1, 8),
       datetime(2021, 1, 10)]

x14 = Series([52, 12, 33, 1, 3], index = x13)
print ("x14 = \n", x14)
print ("-------------------------")

x29 = x14.resample('D').mean()
print ("x29 = \n", x29)
print ("-------------------------")