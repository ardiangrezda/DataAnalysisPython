# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:36:53 2021

@author: msi1
"""

import numpy as np

def Func4(x, y, p):
    d = x - y
    return sum(abs(d) ** p)

x14 = np.array([6, 3, 2, 11])
x15 = np.array([1, 3, 7, 4])

x16 = Func4(x14, x15, 2)

x17 = Func4(p=2, x=x14, y = x15)

print ("x16 = ", x16, " x17 = ", x17)
