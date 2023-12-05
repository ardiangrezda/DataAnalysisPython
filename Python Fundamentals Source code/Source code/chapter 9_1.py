# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 06:23:58 2022

@author: msi1
"""
import pandas as pd
x1 = pd.read_csv('C:/Users/msi1/ex1.csv')
print ("x1 = \n", x1)
print ("------------------------")

x2 = pd.read_csv('ex1.csv', sep=',')
print ("x2 = \n", x2)
print ("------------------------")

x3 = pd.read_csv('ex2.csv', header=None)
print ("x3 = \n", x3)
print ("------------------------")

x4 = pd.read_csv('ex2.csv', names=['a', 'b','c',
                                   'd','message'])
print ("x4 = \n", x4)
print ("------------------------")

x5 = ['a', 'b', 'c', 'd', 'message']
x6 = pd.read_csv('ex2.csv',names=x5, index_col='message')
print ("x6 = \n", x6)
print ("------------------------")

x7 = pd.read_csv('ex3.csv', index_col=['key1','key2'])
print ("x7 = \n", x7)
print ("------------------------")

x8 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
print ("x8 = \n", x8)
print ("------------------------")

x9 = pd.read_csv('ex5.csv')
print ("x9 = \n", x9)
print ("------------------------")

x10 = pd.read_csv('ex5.csv', na_values=['NULL'])
print ("x10 = \n", x10)
print ("------------------------")
