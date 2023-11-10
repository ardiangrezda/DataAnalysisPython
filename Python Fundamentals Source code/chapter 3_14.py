# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 06:31:10 2021

@author: msi1
"""

from numpy import *
x = reshape(arange(0, 21), (7, 3))
y = array([6, 3, 2])

print ("1)")
print ("x = \n", x)
print ("-------------------------")
print ("y = \n", y)
print ("-------------------------")

y1 = x * y
y2 = x / y

print ("y1 = \n", y1)
print ("-------------------------")
print ("y2 = \n", y2)
print ("-------------------------")

print ("2)")
x1 = array([
    [3, 5, 6],
    [12, 2, 11],
    [9, -1, 0]
    ])
x2 = array([
    [7, 15, 2],
    [-12, 1, -11],
    [4, -1, 4]
    ])
print ("x1 = \n", x1)
print ("-------------------------")
print ("x2 = \n", x2)
print ("-------------------------")

x3 = x1 * x2
x4 = transpose(x1)
x5 = transpose(x1 * x2)
print ("x3 = \n", x3)
print ("-------------------------")
print ("x4 = \n", x4)
print ("-------------------------")
print ("x5 = \n", x5)
print ("-------------------------")

print ("3)")
x6 = arange(-4, 10)
print ("x6 = \n", x6)
print ("-------------------------")

x7 = arange(4, 10, 0.35)
print ("x7 = \n", x7)
print ("-------------------------")

x8 = reshape(arange(1, 10, 0.25), (6, 6))
print ("x8 = \n", x8)
print ("-------------------------")

x9 = x8[ix_((4, 5),(3, 1))]
print ("x9 = \n", x9)
print ("-------------------------")

print ("4)")
from numpy.random import *
x10 = randn(4, 5)
print ("x10 = \n", x10)
print ("-------------------------")

x11 = floor(x10[0])
print ("x11 = \n", x11)
print ("-------------------------")

x12 = around(x10[1], 2)
print ("x12 = \n", x12)
print ("-------------------------")

x13 = sum(x10, 0)
print ("x13 = \n", x13)
print ("-------------------------")

x14 = product(x10, 1)
print ("x14 = \n", x14)
print ("-------------------------")

x15 = sort(x10, None)
print ("x15 = \n", x15)
print ("-------------------------")

x10.sort(0)
print ("x10 = \n", x10)
print ("-------------------------")

x16 = x10.max(1)
print ("x16 = \n", x16)
print ("-------------------------")

x10[1][1] = nan
x17 = nansum(x10, 0)
print ("x17 = \n", x17)
print ("-------------------------")
