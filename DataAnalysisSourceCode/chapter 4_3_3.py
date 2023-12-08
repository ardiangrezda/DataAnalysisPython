# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 07:05:22 2022

@author: msi1
"""

import numpy as np
import matplotlib.pyplot as plt
x7 = np.arange(5)
x8 = np.array([4, 2, 6, 1, 4])

colors=['blue', 'yellow', 'magenta', 'red', 'green']
plt.barh(x7, x8, height=0.5, color=colors, edgecolor='#000000', linewidth=6)