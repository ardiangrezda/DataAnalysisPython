# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 06:15:18 2022

@author: msi1
"""
import matplotlib.pyplot as plt
from pandas import *
from numpy import *

fig, axes = plt.subplots(2,1)
x25 = Series(linspace(1, 5, 10), index=list('abcdefghij'))
x25.plot(kind='bar', ax=axes[0], color='b')
x25.plot(kind='barh', ax=axes[1], color='r')

x26 = arange(1,4)
x27 = arange(3,6)
x28 = arange(3, 0, -1)
x29 = arange(5, 2, -1)
x30 = array([x26, x27, x28, x29])

x31 = DataFrame(x30, index=['one','two','three', 'four'],
                columns=Index(['A','B','C'], name='Genus'))

x31.plot(kind='bar')
