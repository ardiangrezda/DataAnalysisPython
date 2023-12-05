# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 07:05:57 2022

@author: msi1
"""

import pandas as pd
import numpy as np

x38 = pd.DataFrame(np.arange(6).reshape((2,3)),
                   index=pd.Index(['Ohio','Colorado'],name='state'),
                   columns=pd.Index(['one','two','three'],name='number'))

print ("x38 = \n", x38)
print ("---------------------")


x39 = x38.stack()
print ("x39 = \n", x39)
print ("---------------------")


x40 = x39.unstack()
print ("x40 = \n", x40)
print ("---------------------")
