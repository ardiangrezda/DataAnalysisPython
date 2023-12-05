# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:13:09 2022

@author: msi1
"""

from pandas import *
import numpy as np
x22 = np.arange(1, 100, 10)
x23 = Series(np.log10(x22), index=x22)
x23.plot()

x24 = DataFrame(np.random.randn(10, 4).cumsum(0),
                columns=['A','B','C','D'],
                index=np.arange(0, 100, 10))
x24.plot()