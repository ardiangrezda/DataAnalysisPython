# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 06:55:17 2022

@author: msi1
"""

from matplotlib.pyplot import figure, plot, bar, pie, draw, scatter
from numpy import sqrt, arange, array
import seaborn as sns

colors = sns.dark_palette("skyblue", 5, reverse=True)

fig = figure(figsize=(12,10))
ax = fig.add_subplot(2,2,1)
x10 = array([3, 1, 1.2, 1.9, 2, 3.2, 9])
plot(x10)
ax.set_title("Subgraph no. 1")


x11 = arange(4)
x12 = array([2, 4, 6, 8])
ax = fig.add_subplot(2, 2, 2)
bar(x11, x12)
ax.set_title("Subgraph no. 2")


x13 = [0.2, 0.25, 0.15, 0.22, 0.18]
ax = fig.add_subplot(2, 2, 3)
pie(x13, colors=colors)
ax.set_title("Subgraph no. 3")

x14 = arange(7)
x15 = array([6, 2, 3, -1, -3, 0, 1])
ax = fig.add_subplot(2, 2, 4 )
scatter(x14, x15)
ax.set_title("Subgraph no. 4")
draw()