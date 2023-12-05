# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 06:06:35 2021

@author: msi1
"""

from pandas import *
x11 = {'state': ['Germany', 'Germany', 'France', 'France','France'],
       'year': [2020, 2021, 2022, 2021, 2020],
       'Statistics': [1.5, 1.7, 3.6, 2.4, 2.9]}

x12 = DataFrame(x11)

print ("x12 = \n", x12)

x13 = DataFrame(x11, 
                columns = ['year', 'state', 'Statistics', 'debt'],
                index = ['one', 'two', 'three', 'four', 'five'])
print ("--------------------------")
print ("x13 = \n", x13)

print ("---------------------------")
print ("x13.columns = ", x13.columns)

print ("---------------------------")
print ("x13.state = \n", x13.state)

x13['debt'] = 21

print ("--------------------------")
print ("After assigning debt, x13 = \n", x13)

x14 = Series([-11, -1, 7], index = ['two', 'four', 'five'])

x13['debt'] = x14
print ("--------------------------")
print ("After assigning column debt to Series, x13 = \n", x13)

x13['East'] = x13.state == 'Germany'
print ("--------------------------")
print ("Creating new column, x13 = \n", x13)

del x13['East']
print ("--------------------------")
print ("Deleting column, x13 = \n", x13)

x15 = {'Italy' : {2019: 2.4, 2020: 2.9} ,
       'Germany': {2018: 1.5, 2019:1.7, 2020:3.6}
    }
x16 = DataFrame(x15)
print ("--------------------------")
print ("x16 = \n", x16)

