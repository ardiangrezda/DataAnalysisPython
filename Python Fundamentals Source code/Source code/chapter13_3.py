# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 07:30:30 2022

@author: msi1
"""

from datetime import datetime

x6 = datetime(2021, 1, 3)

print ("str (x6) = ", str(x6))
print ("---------------------------")

print ("x6.strftime('%Y-%m-%d') = ", 
       x6.strftime("%Y-%m-%d"))
print ("---------------------------")

x7 = '2021-01-03'
x8 = datetime.strptime(x7, "%Y-%m-%d" )
print ("x7 = ", x7)
print ("---------------------------")
print ("x8 = ", x8)
print ("---------------------------")

from dateutil.parser import parse

x9 = parse('2011-01-03')
print ("x9 = ", x9)
print ("---------------------------")

x10 = parse('Jan 31, 2017 10:45 PM')
print ("x10 = ", x10)
print ("---------------------------")

import pandas as pd
x11 = ['7/6/2020', '8/6/2020']
x12 = pd.to_datetime(x11)

print ("x12 = ", x12)
print ("---------------------------")

















