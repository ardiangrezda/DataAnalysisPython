# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:17:27 2021

@author: msi1
"""

from pandas import *
import numpy as np

x42 = DataFrame(np.arange(-4, 8).reshape((4,3)),
        columns = list('bde'),
        index = ['England', 'France', 'Germany', 'Portugal'])

print ("x42 = \n", x42)
print ("-----------------------")

x43 = np.abs(x42)
print ("x43 = \n", x43)
print ("-----------------------")

f = lambda x: x.max() - x.min()
x44 = x42.apply(f)
print ("x44 = \n", x44)
print ("-----------------------")

x45 = x42.apply(f, axis=1)
print ("x45 = \n", x45)
print ("-----------------------")
