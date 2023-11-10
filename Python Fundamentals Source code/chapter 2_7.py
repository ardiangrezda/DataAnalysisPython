# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 07:01:33 2021

@author: msi1
"""
from numpy import array
x27 = array([[0.0]*3]*4)

print ("x27 = \n", x27)
print ("-------------------------")

x27[0, :] = array([9, 8, 7])

print ("After first assignement, x27 = \n", x27)
print ("-------------------------")

x27[::2, ::2] = array([[11.0, 22], [33, 44]])
print ("After second assignement, x27 = \n", x27)
print ("-------------------------")
