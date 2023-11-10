# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 07:32:18 2021

@author: msi1
"""

def square(x):
    return x**2

x1 = 2
x2 = square(x1)

print ("x1 = ", x1, " x2 = ", x2)

def Func1(x, y):
    return (x - y) ** 2

x3 = 3
x4 = 10
x5 = Func1(x3, x4)
print ("x3 = ", x3, " x4 = ", x4, " x5 = ", x5)

from numpy import *
def Func2(x, y):
    d = x - y
    return sqrt(d)

x6 = array([9, 3, 5])
x7 = array([3, 1, 4])

x8 = Func2(x6, x7)
print ("x6 = ", x6, "\nx7 = ", x7, "\nx8 = ", x8)

def Func3(x, y):
    d = x - y
    return sum(abs(d)), sqrt(d)

x9 = array([9, 12, 5])
x10 = array([3, 4, 2])
x11 = Func3(x9, x10)
print ("x9 = ", x9, "\nx10 = ", x10, "\nx11 = ", x11)

x12, x13 = Func3(x9, x10)
print ("x12 = ", x12, "\nx13 = ", x13)
