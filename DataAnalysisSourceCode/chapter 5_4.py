# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 06:55:21 2022

@author: msi1
"""

import pandas as pd
import numpy as np
x17 = pd.DataFrame({'key':['a','b','a','a','b','c'],
                    'value':range(6)})
x18 = pd.DataFrame({'group_val':[3.5, 7]}, 
                   index=['a','b'])
x19 = pd.merge(x17, x18, left_on='key', right_index=True)

print ("x17 = \n", x17)
print ("-------------------------")
print ("x18 = \n", x18)
print ("-------------------------")
print ("x19 = \n", x19)
print ("-------------------------")

x20 = pd.DataFrame({'key1':['Ohio','Ohio', 'Ohio', 'Nevada','Nevada'],
                    'key2':[2000, 2001, 2002, 2001, 2002],
                    'data':np.arange(5)})
x21 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1','event2'])

print ("x20 = \n", x20)
print ("-------------------------")
print ("x21 = \n", x21)
print ("-------------------------")
x22 = pd.merge(x20, x21, left_on=['key1','key2'], right_index=True)
print ("x22 = \n", x22)
print ("-------------------------")

x23 = pd.DataFrame([[1,2],[3,4], [5,6]], 
                   index=['a','c','e'],
                   columns=['Ohio','Nevada'])
x24 = pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],
                   index=['b','c','d','e'],
                   columns=['Missouri','Alabama'])
print ("x23 = \n", x23)
print ("-------------------------")
print ("x24 = \n", x24)
print ("-------------------------")

x25 = x23.join(x24, how='outer')
print ("x25 = \n", x25)
print ("-------------------------")















