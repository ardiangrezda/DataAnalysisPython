# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:38:41 2022

@author: msi1
"""

import matplotlib.pyplot as plt
from numpy import *

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x21 = arange(1, 10, 0.3)
ax.plot(log(x21),'k', label='log')
ax.plot(sin(x21), 'b--', label='sin')
ax.plot(cos(x21), 'r.', label='cos')
ax.legend(loc='best')