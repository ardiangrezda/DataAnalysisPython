# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 06:33:58 2021

@author: msi1
"""

x1 = 1
if x1 < 5:
    x1 += 1
else:
    x1 -= 1
print ("x1 = ", x1)

x2 = 7
if x2 < 5:
    x2 = x2 + 1
elif x2 > 5:
    x2 = x2 - 1
else:
    x2 = x2 * 2
print ("x2 = ", x2)
