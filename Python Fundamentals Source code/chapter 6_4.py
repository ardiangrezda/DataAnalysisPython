# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:03:48 2021

@author: msi1
"""

import numpy as np
class DataVis(object):
    def __init__(self, data=None, dataSize = 0):
        self.data = data
        self.dataSize = dataSize
    @property
    def PropData(self):
        return self.data
    @PropData.setter
    def PropData(self, value):
        print ("value = ", value, " dataSize = ", self.dataSize)
        if np.size(value,0) < self.dataSize:
            raise ValueError("value should be smaller than dataSize")
        self.data = value

x6 = np.array([[10, 11, 12, 14, 16]])

x7 = DataVis()
print ("x7 = ", x7.__dict__)

x8 = DataVis(x6)
print ("x8 = ", x8.__dict__)

x9 = DataVis(x6, 2)
print ("x9 = ", x9.__dict__)

x10 = DataVis(dataSize=1)
print ("x10 = ", x10.__dict__)

x11 = DataVis(x6, 2)
print ("x11 = ", x11.__dict__)

x12 = np.array([[10, 11, 12, 14]])
x13 = np.array([[10, 11, 12, 14], 
                [1, 2, 3, 4], 
                [3, 4, 5, 6]])

x11.PropData = x13
#print ("After properties change, x11 = ", x11.__dict__)

x11.PropData = x12