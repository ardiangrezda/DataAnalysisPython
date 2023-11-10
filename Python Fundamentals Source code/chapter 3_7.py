# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 07:04:16 2021

@author: msi1
"""

from numpy.random import *
from numpy import *
x27 = randn(5)
x28 = around(x27)

print ("x27 = ", x27)
print ("x28 = ", x28)

x29 = around(x27, 2)
print ("x29 = ", x29)

x30 = floor(x27)
print ("x30 = ", x30)

x31 = ceil(x27)
print ("x31 = ", x31)
