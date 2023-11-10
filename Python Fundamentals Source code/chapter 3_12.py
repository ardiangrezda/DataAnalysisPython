# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 07:24:03 2021

@author: msi1
"""

from numpy import *

x47 = arange(-3.0, 5)

print ("x47 = ", x47)
print ("------------------------")

x48 = x47 > 0

print ("x48 = ", x48)
print ("------------------------")

x49 = x47 < 2
print ("x49 = ", x49)
print ("------------------------")

x50 = logical_and(x48, x49)
print ("x50 = ", x50)
print ("------------------------")

x51 = logical_xor(x48, x49)
print ("x51 = ", x51)
print ("------------------------")

