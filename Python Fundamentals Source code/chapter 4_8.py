# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 06:53:52 2021

@author: msi1
"""

x22 = ['d', '19', '14.1', '43.b']

for i in x22:
    try:
        x23 = float(i)
        print ("x23 = ", x23)
    except ValueError:
        print ("Not convertible to a float")

