# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:30:21 2022

@author: msi1
"""

import pandas as pd

x58 = pd.read_csv('macrodata.csv')

x59 = pd.PeriodIndex(year=x58.year,
                     quarter=x58.quarter,
                     freq='Q-DEC')

print ("x59 = ", x59)
print ("-------------------------")

x58.index = x59

print ("x58.infl.head() = \n", x58.infl.head())
print ("-------------------------")
