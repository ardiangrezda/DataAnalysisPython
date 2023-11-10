# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 07:20:23 2021

@author: msi1
"""

import numpy as np

def Func7(x, y, p=2, **kwargs):
    d = x - y
    print ("Number of kwargs ", len(kwargs))
    for key in kwargs:
        print ("key : ", key, " value:", kwargs[key])
    return sum(abs(d) ** p)

x28 = np.array([6, 3, 2, 11])
x29 = np.array([1, 3, 7, 4])

x30 = Func7(x28, x29, kword1=1, kword2=3.2)
print ("x30 = ", x30)

x31 = Func7(x28, x29, kword1=1, kword2=3.2, p=0)
print ("x31 = ", x31)
