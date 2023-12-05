# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:02:10 2022

@author: msi1
"""

from datetime import datetime

x1 = datetime.now()
print ("x1 = ", x1)
print ("----------------------------")

x2 = datetime(2021, 1, 7) - datetime(2018, 6, 24, 8, 15)
print ("x2 = ", x2)
print ("----------------------------")

from datetime import timedelta
x3 = datetime(2021, 1, 7)
x4 = x3 + timedelta(12)
print ("x3 = ", x3)
print ("----------------------------")
print ("x4 = ", x4)
print ("----------------------------")

x5 = x3 - 2 * timedelta(12)
print ("x5 = ", x5)
print ("----------------------------")
