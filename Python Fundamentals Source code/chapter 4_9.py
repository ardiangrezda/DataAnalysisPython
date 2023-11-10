# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 07:19:47 2021

@author: msi1
"""

from numpy import *
x24 = arange(5.0)
x25 = []
for i in range(len(x24)):
    x25.append(square(x24[i]))

print ("x25 = ", x25)
print ("--------------------")

x26 = [square(x24[i])         for i in range(len(x24))]

print ("x26 = ", x26)
print ("--------------------")

x27 = arange(6)
x28 = []
for i in range(len(x27)) :
    if i % 2 == 0: 
        x28.append(x27[i]**3)
print ("x28 = ", x28)
print ("--------------------")

x29 = [x27[i]**3      for i in range(len(x27))  if i % 2 == 0]
print ("x29 = ", x29)
print ("--------------------")

x30 = arange(5)
x31 = arange(3)
x32 = []
for i in range(len(x30)):
    for j in range(len(x31)):
        x32.append(x30[i] + x31[j])
print ("x32 = ", x32)
print ("--------------------")

x33 = [x30[i]+x31[j]                 for i in range(len(x30))   for j in range(len(x31))]
print ("x33 = ", x33)
print ("--------------------")
