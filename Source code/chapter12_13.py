# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 06:57:53 2022

@author: msi1
"""

import pandas as pd

a = pd.read_csv('titanic.csv')
print ("a = \n", a)
print ("----------------------")

b = a[['pclass','sex', 'age','fare', 'embarked']]
print ("b = \n", b)
print ("----------------------")

c = b.groupby('sex').count()
print ("c = \n", c)
print ("----------------------")

d = b.groupby(['sex', 'embarked']).count()
print ("d = \n", d)
print ("----------------------")

e = d.unstack()
print ("e = \n", e)
print ("----------------------")

f = b.agg(['min','max','sum','count', 'size'])
print ("f = \n", f)
print ("----------------------")

g = b.groupby(['sex', 'embarked'], as_index=False).count()
print ("g = \n", g)
print ("----------------------")