# -*- coding: utf-8 -*-
"""
Created on Mon May  2 07:49:31 2022

@author: msi1
"""

from pandas import *
x44 = DataFrame({'food':['bacon','pulled pork', 'bacon',
                'Pastrami', 'corned beef', 'Bacon'],
                 'onces':[4, 3, 12, 6, 7.5, 8]})
print ("x44 = \n", x44)
print ("----------------------------")

meat_to_animal = {'bacon':'pig', 'pulled pork': 'pig',
                  'pastrami': 'cow',
                  'corned beef': 'cow'}

x44['animal'] = x44['food'].map(str.lower).map(meat_to_animal)

print ("After transformation, x44 = \n", x44)
print ("----------------------------")

x44['animal lambda'] = x44['food'].map(lambda x: meat_to_animal[x.lower()])
print ("After applying lambda, x44 = \n", x44)
print ("----------------------------")
