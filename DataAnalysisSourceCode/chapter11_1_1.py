# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:07:56 2022

@author: msi1
"""

import pandas as pd
x1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'], 
                   'data1':range(7)})
x2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print ("x1 = \n", x1)
print ("----------------------")
print ("x2 = \n", x2)
print ("----------------------")

x3 = pd.merge(x1, x2)
print ("x3 = \n", x3)
print ("----------------------")

x4 = pd.merge(x1, x2, on='key')
print ("x4 = \n", x4)
print ("----------------------")


x5 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'], 
                   'data1':range(7)})
x6 = pd.DataFrame({'rkey':['a','b','d'], 'data2':range(3)})
x7 = pd.merge(x5, x6, left_on='lkey',right_on='rkey' )
print ("x5 = \n", x5)
print ("----------------------")
print ("x6 = \n", x6)
print ("----------------------")
print ("x7 = \n", x7)
print ("----------------------")

x8 = pd.merge(x1, x2, how='outer')
print ("x1 = \n", x1)
print ("----------------------")
print ("x2 = \n", x2)
print ("----------------------")
print ("x8 = \n", x8)
print ("----------------------")


x9 = pd.DataFrame({'key':['b','b', 'a', 'c', 'a','b'], 
                'data1':range(6)})
x10 = pd.DataFrame({'key':['a', 'b','a','b','d'],
                 'data2':range(5)})

x11 = pd.merge(x9, x10, on='key', how='left')
print ("x9 = \n", x9)
print ("----------------------")
print ("x10 = \n", x10)
print ("----------------------")
print ("x11 = \n", x11)
print ("----------------------")

x12 = pd.DataFrame({'key1':['foo','foo','bar'], 
                 'key2':['one','two','one'],
                 'lval':[1, 2, 3]})
x13 = pd.DataFrame({'key1':['foo','foo','bar','bar'], 
                 'key2':['one','one','one','two'],
                 'rval':[4, 5, 6, 7]})
x14 = pd.merge(x12, x13, on=['key1','key2'], how='outer')

print ("x12 = \n", x12)
print ("----------------------")
print ("x13 = \n", x13)
print ("----------------------")
print ("x14 = \n", x14)
print ("----------------------")

x15 = pd.merge(x12, x13, on='key1')
print ("x12 = \n", x12)
print ("----------------------")
print ("x13 = \n", x13)
print ("----------------------")
print ("x15 = \n", x15)
print ("----------------------")

x16 = pd.merge(x12, x13, on='key1', 
               suffixes=('_left','_right'))
print ("x12 = \n", x12)
print ("----------------------")
print ("x13 = \n", x13)
print ("----------------------")
print ("x16 = \n", x16)
print ("----------------------")


