# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 07:09:27 2021

@author: msi1
"""

## Task 1
def func(x):
    if x > 15:
        print ("Larger than ", x)
    elif x < 0:
        print ("Smaller than ", x)
    else:
        print ("between 0 and 15")

x = 6
func(x)

x = -1
func(x)

x = 20
func(x)

############################
### Task nr. 2
from numpy import *
x = array([
     [11., 1, 4 ],
     [13, 7, 5],
     [26, -7, 8],
     [99, 10, -11],
     [12, 33, -1],
     [15, 6, 17]
     ]
    )

print ("a) before x = \n", x)
print ("-------------------")
for i in range(size(x, 0)):
    if i % 2 == 0:
        x[i][0] = x[i][0] * x[i][0]
print ("a) after x = \n", x)
print ("-------------------")

print ("b) before x = \n", x)
print ("-------------------")
for i in range(size(x, 0)): 
    if i % 2 == 1:
        x[i][2] = - x[i][2]
print ("b) after x = \n", x)
print ("-------------------")

print ("c) before x = \n", x)
print ("-------------------")
for i in range(size(x,0)):
    if i == 1:
        for j in range(size(x, 1)):
            x[i][j] = - x[i][j] / 7
print ("c) before x = \n", x)
print ("-------------------")
            
#### Task nr 3
from numpy.random import *
x = randn(100)
count1 = 0
count2 = 0
count3 = 0

for i in x:
    if i > 0.3:
        count1 = count1 + 1
    elif i < -0.4:
        count2 = count2 + 1
    else:
        count3 = count3 + 1
print ("count1 = ", count1)
print ("count2 = ", count2)
print ("count3 = ", count3)


##### Task nr 4
x = [3, 1, 45, 5, 1, -4, 1, 66, 12, -22, -2]

z1 = []
for i in range(len(x)):
    if i % 2 == 1:
        z1.append(x[i] * 100)
print ("-------------------")
print ("z1 = ", z1)

z2 = [x[i]/7           for i in range(len(x)) if i % 2 == 0]
print ("-------------------")
print ("z2 = ", z2)
