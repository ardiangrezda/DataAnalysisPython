# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 05:57:36 2022

@author: msi1
"""

from numpy import *
from pandas import *
import numpy as np

cattle = [6000, 7000, 9000, 1000, 2000, 9000, 10000 ]
chicken  = [17000, 22000, 69000, 51000, 22000, 39000, 410000]
sheep = [88000, 29000, 19000, 41000, 12000, 19000, 480000 ]

anim = np.array([cattle,chicken, sheep ]).T

country = ['China', 'India', 'Turkey', 'Iran', 
           'Thailand', 'Pakistan', 'Indonesia']

frame = DataFrame(anim, index = country, 
                  columns=['cattle','chicken','sheep'])
print ("frame = \n", frame)
print ("-------------------------")

x1 = frame.loc[['Turkey','Iran'],['cattle','chicken']]
print ("x1 = \n", x1)
print ("-------------------------")

min1 = lambda x: x.min()
max1 = lambda x: x.max()

x2 = frame.apply(min1)
x3 = frame.apply(max1)
print ("x2 = \n", x2)
print ("-------------------------")
print ("x3 = \n", x3)
print ("-------------------------")

x4 = frame.sort_index()
print ("x4 = \n", x4)
print ("-------------------------")

x5 = frame.sort_index(ascending=False)
print ("x5 = \n", x5)
print ("-------------------------")

x6 = frame.sort_values(by=['sheep'])
print ("x6 = \n", x6)
print ("-------------------------")

x7 = frame.sum()
x8 = frame.mean()
print ("x7 = \n", x7)
print ("-------------------------")
print ("x8 = \n", x8)
print ("-------------------------")

x9 = frame.idxmax()
print ("x9 = \n", x9)
print ("-------------------------")

frame.loc['USA'] = [10000, nan, 30000]
frame.loc['Canada'] = 12000

print ("New frame = \n", frame)
print ("-------------------------")

frame2 = frame.dropna()
print ("frame2 = \n", frame2)
print ("-------------------------")

frame = frame.fillna(frame.mean())
print ("After refilling, frame = \n", frame)
print ("-------------------------")

