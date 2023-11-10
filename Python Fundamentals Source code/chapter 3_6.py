# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 07:07:56 2021

@author: msi1
"""

from numpy import *
x24 = reshape(arange(25), (5, 5))

print ("x24 = \n", x24)
print ("--------------------------")

x25 = x24[ix_([2, 3], [0, 1, 2])]
print ("x25 = \n", x25)
print ("--------------------------")

x26 = x24[2:4, :3]
print ("x26 = \n", x26)
print ("--------------------------")
