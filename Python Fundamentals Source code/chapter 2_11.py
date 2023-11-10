# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 08:27:43 2021

@author: msi1
"""

from numpy import *

u = array([1, 1, 2, 3, 5, 8])
print ("u = ", u)
print ("--------------------------")

x = array([
    [1, 0],
    [0, 1]
    ])
print ("x = \n", x)
print ("--------------------------")

y = array([
    [1, 2],
    [3, 4]
    ])
print ("y = \n", y)
print ("--------------------------")

z = array([
    [1, 2, 1, 2],
    [3, 4, 3, 4],
    [1, 2, 1, 2]
    ])
print ("z = \n", z)
print ("--------------------------")

w = array([
    [x, x],
    [y, y]
    ])
print ("w = \n", w)
print ("--------------------------")

x0 = [[1, 21], [-1, -2]]
x1 = array(x0)
print ("x1 = \n", x1)
print ("--------------------------")

x2 = array(x0, dtype='float')
print ("x2 = \n", x2)
print ("--------------------------")

x3 = array(x0, dtype='float64')
print ("x3 = \n", x3)
print ("--------------------------")

x4 = array(x0, dtype='int32')
print ("x4 = \n", x4)
print ("--------------------------")

x5 = array(x0, dtype='uint32')
print ("x5 = \n", x5)
print ("--------------------------")

x6 = array(x0, ndmin=3)
print ("x6 = \n", x6)
print ("--------------------------")
print ("ndim(x6) = ", ndim(x6))
print ("--------------------------")

x7 = array(x0, ndmin=4)
print ("x7 = \n", x7)
print ("--------------------------")
print ("ndim(x7) = ", ndim(x7))
print ("--------------------------")

x8 = eye(4)
print ("x8 = \n", x8)
print ("--------------------------")
x9 = ones((4, 4))
print ("x9 = \n", x9)
print ("--------------------------")

x8[1][2] = 10
x8[3][2] = 6
x8[1][0] = -1
x9[0][2] = 7
x9[1][3] = -4
print ("After modification, x8 = \n", x8)
print ("--------------------------")
print ("After modification x9 = \n", x9)
print ("--------------------------")

x10 = x8 * x9
print ("x10 = \n", x10)
print ("--------------------------")
