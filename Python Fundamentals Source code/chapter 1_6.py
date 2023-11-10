# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 09:26:08 2023

@author: msi1
"""

x10 = [1, 3, 9, 11, 13, 19, 21]

print ("x10 = ", x10)

x10.append(23)

print ("After append, x10 = ", x10)

print ("Number of elements in the list are: ", len(x10))

x10.extend([2, 4, 6, 8, 10, 12, 2, 8])

print ("After extend, x10 = ", x10)

x10.pop(4)

print ("After pop, x10 = ", x10)

x10.remove(19)

print ("After remove, x10 = ", x10)

print ("Number 2 appears ", x10.count(2), " times in the list")

del x10[:5]

print ("After del, x10 = ", x10)
