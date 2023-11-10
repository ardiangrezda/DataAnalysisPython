# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 07:05:31 2021

@author: msi1
"""

from numpy import *
x30 = arange(5)
x34 = {i: square(i)             for i in x30}
print ("x34 = ", x34)

x35 = tuple(i**3            for i in x30)
print ("x35 = ", x35)
