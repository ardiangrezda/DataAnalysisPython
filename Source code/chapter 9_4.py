# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 06:37:24 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x22 = pd.read_csv('ex5.csv')
print ("x22 = \n", x22)
print ("------------------------")

x22.to_csv("ex7.csv")

x23 = pd.date_range("1/1/2000", periods=7)
x24 = pd.Series(np.arange(7), index=x23)
print ("x24 = \n", x24)
print ("------------------------")

x24.to_csv('ex8.csv',header=False)
