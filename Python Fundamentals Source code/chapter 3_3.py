# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 07:33:35 2021

@author: msi1
"""

from numpy import reshape, arange
x13 = reshape(arange(15), (3, 5))
print ("x13 = \n", x13)
print ("---------------------------------")

x14 = reshape(arange(10, 25), (3, 5))
print ("x14 = \n", x14)
print ("---------------------------------")

x15 = x13 + x14
print ("x15 = \n", x15)
print ("---------------------------------")
