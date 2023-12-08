# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:27:36 2022

@author: msi1
"""

import pandas as pd
x25 = pd.ExcelFile('ex1.xlsx')
x26 = x25.parse("Sheet1")

print ("x26 = \n", x26)
print ("--------------------------")