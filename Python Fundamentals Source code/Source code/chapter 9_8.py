# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 06:37:31 2022

@author: msi1
"""

import pandas as pd

df_1880 = pd.read_csv('yob1880.txt', names=['name', 
            'gender', 'total'])
df_1881 = pd.read_csv('yob1881.txt', names=['name', 
            'gender', 'total'])
df_1882 = pd.read_csv('yob1882.txt', names=['name', 
            'gender', 'total'])

total_female = df_1880[df_1880.gender == 'F'].total.sum()
print ("total_female = ", total_female)

total_male = df_1880[df_1880.gender == 'M'].total.sum()
print ("total_male = ", total_male)

total_Alice = int(df_1880[df_1880.name == 'Alice'].total.values)
print ("total_Alice = ", total_Alice)

print ("Before df_1880[1180:1200] = \n", df_1880.loc[1180:1200])
print ("-----------------------------")
df_1880.loc[1180:1200].name = 'ABC'
print ("After df_1880[1180:1200] = \n", df_1880.loc[1180:1200])
print ("-----------------------------")

total_grace = df_1880[df_1880.name == 'Grace'].total.sum() + \
    df_1881[df_1881.name == 'Grace'].total.sum() + \
    df_1882[df_1882.name == 'Grace'].total.sum()
print ("total_grace = ", total_grace)
print ("----------------------------")
print ("df_1882.tail(15) = \n", df_1882.tail(15))
print ("----------------------------")
