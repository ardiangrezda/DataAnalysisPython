# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:10:19 2021

@author: msi1
"""

from pandas import *

country = Series(["China", "India", "Turkey", "Iran", "Thailand", 
                  "Pakistan", "Indonezia"])
population = [1400, 1350, 82, 81, 70, 212, 267]
female = [699, 700, 43, 39, 36, 109, 140]

frame = DataFrame(population, index=country, columns=['Population'])

print ("frame = \n", frame)
print ("------------------")

frame["female"] = female

print ("After adding column female, frame = \n", frame)
print ("------------------")

frame["male"] = frame["Population"] - frame["female"]
print ("After adding column male, frame = \n", frame)
print ("------------------")

frame["dump"] = frame["male"] * 0.7
print ("After adding column dump, frame = \n", frame)
print ("------------------")

frame["% male"] = frame["male"] * 100 / frame["Population"]
print ("After adding column perc. male, frame = \n", frame)
print ("------------------")

del frame["dump"]
print ("After deleting column dump, frame = \n", frame)
print ("------------------")