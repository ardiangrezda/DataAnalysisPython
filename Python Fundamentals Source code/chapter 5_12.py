# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 05:32:08 2021

@author: msi1
"""

# task nr. 1
def minimum(x):
    xmin = x[0]
    for i in x:
        if i < xmin:
            xmin = i
    return xmin

x1 = [1, 2, 5, -9, 10, 11, 3]

x2 = minimum(x1)
print ("x2 = ", x2)

# task nr 2
from numpy import *
def func1(x, y= 2):
    Z = exp(x) + y
    return Z

x3 = array([1, 5, 9, 11, 23])

x4 = func1(x3)
print ("x4 = ", x4)

def func2(x, y = 3, *args):
    Z = exp(x) + y
    for i in args:
        Z += 4.5 * i
    return Z

x5 = func2(x3)
print ("x5 = ", x5)

x6 = func2(x3, 2)
print ("x6 = ", x6)

x7 = func2(x3, 2, 1, 2, 3)
print ("x7 = ", x7)

def f1(x, y, **kwargs):
    z = x * y
    for i in kwargs:
        z *= kwargs[i]
    return z

x8 = 1
x9 = 2
x10 = f1(x8, x9)
print ("x10 = ", x10)

x11 = f1(x8, x9, k1=10, k2=5)
print ("x11 = ", x11)

def f2(x, y):
    z = x - y
    if z > 0:
        return z
    else:
        return -z
    
x12 = f2(5, 6)
print ("x12 = ", x12)

x13 = f2(5, 3)
print ("x13 = ", x13)

if __name__ == "__main__":
    print("Executed directly =" , f1(x8, x9, k1=10, k2=5))
else:
    print ("Executed using import = ", f2(5, 6))
    
