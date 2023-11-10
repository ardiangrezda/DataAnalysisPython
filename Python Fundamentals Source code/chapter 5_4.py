# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 07:11:31 2021

@author: msi1
"""

import numpy as np
def Func6(x, y, p=2, *args):
    d = x - y
    print ("The first part computes sum(abs(d) ** p)", sum(abs(d) ** p) )
    out = [sum(abs(d) ** p)]
    for p in args:
        print ("Using *args: ", sum(abs(d)** p))
        out.append(sum(abs(d)** p))
    return out

x23 = np.array([6, 3, 2, 11])
x24 = np.array([1, 3, 7 , 4])

x25 = Func6(x23, x24)
print ("x25 = ", x25)
                   
x26 = Func6(x23, x24, 1)
print ("x26 = ", x26)

x27 = Func6(x23, x24, 1, 2, 3, 4, 1.5, 2.5)
print ("x27 = ", x27)
