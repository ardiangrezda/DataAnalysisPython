# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 07:04:31 2022

@author: msi1
"""

from pandas import *
import pandas as pd

def peak_to_peak(arr):
    return arr.max() - arr.min()

x1 = DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':[0.2, 0.25, 0.3, 0.35, 0.4],
                'data2':[1.4, 1.45,1.5, 1.55, 1.6]})

print ("x1 = \n", x1)
print ("------------------------")

x21 = x1.groupby('key1')

x22 = x21.agg(peak_to_peak)
print ("x22 = \n", x22)
print ("------------------------")

x23 = pd.read_csv('tips.csv')

x23['tip_pct'] = x23['tip'] / x23['total_bill']
print ("x23.head(4) = \n", x23.head(4))
print ("------------------------")

x24 = x23.groupby(['sex', 'smoker'])
x25 = x24['tip_pct']
x26 = x25.agg("mean")
print ("x26 = \n", x26)
print ("------------------------")

x27 = x25.agg(['mean', 'std', peak_to_peak])
print ("x27 = \n", x27)
print ("------------------------")

functions = ['count', 'mean', 'max']

x28 = x24['tip_pct', 'total_bill'].agg(functions)
print ("x28 = \n", x28)
print ("------------------------")

x29 = x24.agg({'tip_pct':['min','max','mean','std'], 'size':'sum'})
print ("x29 = \n", x29)
print ("------------------------")


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

x31 = top(x23, n=4)
print ("x31 = \n", x31)
print ("------------------------")

x32 = x23.groupby('smoker').apply(top, 3)
print ("x32 = \n", x32)
print ("------------------------")

x33 = x23[['total_bill','tip', 'smoker', 
           'day']].groupby(['smoker',
        'day']).apply(top, n=1, column='total_bill')

print ("x33 = \n", x33)
print ("------------------------")

x34 = x23[['total_bill','tip_pct', 'smoker', 
           'day']].groupby('smoker', group_keys=False).apply(top, 3)

print ("x34 = \n", x34)
print ("------------------------")













