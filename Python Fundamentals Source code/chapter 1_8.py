# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 06:43:49 2021

@author: msi1
"""

x13 = {'age': 45, 'children': [1, 2], 'plant': 'tomato'}

print ("x13 = ", x13)

print ("x13['age'] = ", x13['age'])

x13['age'] = 'abd'

print ("After modification, x13['age'] = ", x13['age'])

x13['name'] = 'John'

print ("After adding, x13 = ", x13)

del x13['age']

print ("After deleting, x13 = ", x13)
