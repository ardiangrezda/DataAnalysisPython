# -*- coding: utf-8 -*-
"""
Created on Sun May 15 07:40:29 2022

@author: msi1
"""

import pandas as pd

a = pd.read_csv(r"d:\test\train_titanic.csv")
b = pd.read_csv(r"d:\test\test_titanic.csv")

print ("a = \n", a.head())
print ("--------------------------")

print ("b = \n", b.head())
print ("--------------------------")

c = a[['survived','pclass', 'sex','age','fare','embarked']]
d = b[['pclass', 'sex','age','fare','embarked']]

print ("c = \n", c.head())
print ("--------------------------")

print ("d = \n", d.head())
print ("--------------------------")

e = pd.merge(c.head(10), d.tail(10), on='embarked')

print ("e = \n", e)
print ("--------------------------")

c1 = c.set_index('age').head(10)
d1 = d.set_index('age').tail(10)

g = pd.merge(c1, d1, left_index=True,
             right_index=True,how='left')
print ("g = \n", g)
print ("--------------------------")

h1 = pd.concat([a, b])
h2 = pd.concat([a,b], axis=1)
print ("h1 = \n", h1)
print ("--------------------------")
print ("h2 = \n", h2)
print ("--------------------------")
