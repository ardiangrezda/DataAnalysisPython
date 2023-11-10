# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 06:55:32 2021

@author: msi1
"""

import numpy as np

def Func5(x, y, p = 2):
    d = x - y
    return sum(abs(d) ** p)

x18 = np.array([6, 3, 2, 11])
x19 = np.array([1, 3, 7, 4])

x20 = Func5(x18, x19)
x21 = Func5(x18, x19, 1)
x22 = Func5(x18, x19, 2)

print ("x20 = ", x20, " x21 = ", x21, " x22 = ", x22)