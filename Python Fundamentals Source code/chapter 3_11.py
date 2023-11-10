# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 07:15:13 2021

@author: msi1
"""

from numpy import *
x44 = array([
    [1, 4],
    [-2, -1]
            ])
print ("x44 = \n", x44)
print ("-----------------------")

x45 = x44 > 0 
print ("x45 = \n", x45)
print ("-----------------------")

x46 = x44 == -1
print ("x46 = \n", x46)
print ("-----------------------")