# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 06:15:23 2022

@author: msi1
"""

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import *
x9 = [0.2, 0.4, 0.25, 0.15]

expPie = array([.2, 0, 0, 0])
colPie = sns.dark_palette("skyblue", 4, reverse=True)
labPie = ['One', 'Two', 'Three', 'Four']
plt.pie(x9, explode=expPie, colors=colPie, labels=labPie,
        autopct='%2.0f', shadow=True)