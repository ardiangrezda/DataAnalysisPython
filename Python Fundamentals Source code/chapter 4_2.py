# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 06:22:15 2021

@author: msi1
"""

x3 = 0

for i in range(5):
    x3 += i
    print ("i = ", i, " x3 = ", x3)

print ("x3 = ", x3)
print ("---------------------")

from numpy import *
x4 = 0
x5 = linspace(0, 50, 5)
for i in x5:
    x4 += i
    
print ("x4 = ", x4)
print ("---------------------")


x6 = 0
x7 = list(arange(-5, 4))
for i in x7:
    x6 += i
print ("x6 = ", x6)
print ("---------------------")


x8 = 0
for i in range(4):
    for j in range(5):
        x8 += j

print ("x8 = ", x8)
print ("---------------------")

from numpy.random import *
x9 = randn(40)
x10 = 0
for i in x9:
    if i < 0 :
        x10 += 1
print ("x10 = ", x10)
print ("---------------------")

        