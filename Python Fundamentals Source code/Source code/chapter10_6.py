# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 07:24:17 2022

@author: msi1
"""

import matplotlib.pyplot as plt
from numpy import arange
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x16 = arange(1, 10, 0.35)
x17 = arange(10, 4, -0.2)
x18 = arange(4, 15, 0.3)
x19 = np.concatenate((x16, x17, x18))
x20 = arange(len(x19))
ax.scatter(x20, x19, s=3, marker='s', alpha=0.5)
ticks = ax.set_xticks([0, 25, 50, 75, 100])
labels = ax.set_xticklabels(['one', 'two', 'three',
                             'four', 'five'], rotation=30,
                            fontsize='small')
ax.set_title("My first matplolib graph")
ax.set_xlabel("Stages")
ax.set_ylabel("Y axis")
ax.set_yticks([2, 6, 10, 14])