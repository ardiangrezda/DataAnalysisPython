# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 07:36:03 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x26 = pd.Series([0,1], index=['a','b'])
x27 = pd.Series([2, 3, 4], index=['c','d','e'])
x28 = pd.Series([5,6], index=['f','g'])
x29 = pd.concat([x26, x27, x28])
print ("x26 = \n", x26)
print ("----------------------")
print ("x27 = \n", x27)
print ("----------------------")
print ("x28 = \n", x28)
print ("----------------------")
print ("x29 = \n", x29)
print ("----------------------")

x30 = pd.concat([x26, x27, x28], axis=1)
print ("x30 = \n", x30)
print ("----------------------")

x31 = pd.concat([x26*5, x28])
print ("x31 = \n", x31)
print ("----------------------")

x32 = pd.concat([x26, x31], axis=1)
print ("x32 = \n", x32)
print ("----------------------")

x33 = pd.concat([x26, x31], axis=1, join='inner')
print ("x33 = \n", x33)
print ("----------------------")

x34 = pd.concat([x26, x26, x28], keys=['one','two','three'])
print ("x34 = \n", x34)
print ("----------------------")

x35 = pd.DataFrame(np.arange(6).reshape(3,2), 
                   index=['a','b','c'],
                   columns=['one','two'])
x36 = pd.DataFrame(5 + np.arange(4).reshape(2,2),
                   index=['a','c'],
                   columns=['three','four'])
print ("x35 = \n", x35)
print ("----------------------")
print ("x36 = \n", x36)
print ("----------------------")

x37 = pd.concat([x35, x36], axis=1, keys=['level1','level2'])
print ("x37 = \n", x37)
print ("----------------------")













