# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:45:31 2022

@author: msi1
"""
import matplotlib.pyplot as plt
import numpy as np
x3 = np.array([-1, 3, 5, 11, 15, 9, 13, 7])
x4 = np.array([2, 4, 6, 8, 10, 12, 14, 16])
plt.plot(x3, x4, alpha=0.5, color='#FF7F00',
         linestyle='-.', linewidth=3, marker='o',
         markeredgecolor='#000000', 
         markeredgewidth=2, markerfacecolor='#FF7F00',
         markersize=20)