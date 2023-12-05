# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:04:00 2022

@author: msi1
"""

from pandas import *
import numpy as np
import pandas as pd

x11 = np.linspace(1, 11, 10000).round(4)
x12 = np.linspace(11, 21, 10000).round(4)
x13 = np.linspace(21, 31, 10000).round(4)
x14 = np.linspace(31, 41, 10000).round(4)
x15 = np.repeat('',10000)
x16 = np.array([x11, x12, x13, x14, x15])
x17 = np.array(['A', 'B', 'C','D','E','F', 'G',
                'H','I','J','K','L'])

x18 = pd.DataFrame(x16.T, columns = ['one','two',
       'three', 'four', 'key'])

for i in x18.index:
    x18.loc[i]['key'] = x17[i % len(x17)]

print ("x18 = \n", x18)
print ("-----------------------")

x18.to_csv('ex6.csv',index=None)

x19 = pd.read_csv('ex6.csv', nrows=5)
print ("x19 = \n", x19)
print ("-----------------------")

x20 = pd.read_csv('ex6.csv', chunksize=1000)
x21 = pd.Series([])

for piece in x20:
    x21 = x21.add(piece['key'].value_counts(),
                  fill_value=0)

x21 = x21.sort_values(ascending=False)
print ("x21 = \n", x21)
print ("-----------------------")
