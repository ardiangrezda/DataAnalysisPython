# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:08:53 2022

@author: msi1
"""

import pandas as pd

x30 = pd.date_range('4/1/2012', '5/1/2012')

print ("x30 = \n", x30)
print ("-------------------------------")

x31 = pd.date_range(start='4/1/2012', periods=10)
print ("x31 = \n", x31)
print ("-------------------------------")

x32 = pd.date_range(end='6/1/2012', periods=10)
print ("x32 = \n", x32)
print ("-------------------------------")

x33 = pd.date_range('1/1/2000', '10/1/2000', freq='BM')
print ("x33 = \n", x33)
print ("-------------------------------")

x34 = pd.date_range('5/2/2012 12:56:31', periods=5)
print ("x34 = \n", x34)
print ("-------------------------------")
