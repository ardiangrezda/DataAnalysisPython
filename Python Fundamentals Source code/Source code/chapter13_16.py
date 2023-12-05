# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 07:30:16 2022

@author: msi1
"""

import numpy as np
import pandas as pd

x69 = pd.DataFrame(np.reshape(np.arange(8), (2,4)),
            index=pd.date_range('1/1/2020', periods=2,
                    freq='W-WED'),
            columns=['USA','Canada','Germany', 'Italy'])

print ("x69 = \n", x69)
print ("----------------------------------------")

x70 = x69.resample('D').mean()
print ("x70 = \n", x70)
print ("----------------------------------------")
