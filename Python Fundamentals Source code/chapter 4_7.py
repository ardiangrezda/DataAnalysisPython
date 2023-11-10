# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:00:12 2021

@author: msi1
"""

from numpy import *

x18 = 0
i = 1

while i < 8 :
    x18 += i
    i += 1
    
print ("x18 = ", x18, " i = ", i)
print ("-----------------------")


x19 = 0
for i in range(0, 8):
    x19 += i

print ("x19 = ", x19, " i = ", i)
print ("-----------------------")

x20 = True; i = 0
x21 = arange(0, 10, 0.4)

while x20:
    if x21[i] == 4:
        break
    print ("x21[i] = ", x21[i])
    i += 1
    
print ("i = ", i, "x21[i] = ", x21[i])
print ("-----------------------")