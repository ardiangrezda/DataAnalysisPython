# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 07:04:41 2021

@author: msi1
"""

class DataVis(object):
    def __init__(self, data=None, dataSize = 0):
        self.data = data
        self.dataSize = dataSize
    def AddAditionalAtrib(self):
        self.additional = "There is another atribute added"

from numpy import *
x1 = array([[10, 11, 12, 14, 16]])
x2 = DataVis()
print ("x2 = ", x2.__dict__)

x3 = DataVis(x1)
print ("x3 = ", x3.__dict__)

x4 = DataVis(x1, 2)
print ("x4 = ", x4.__dict__)

x5 = DataVis(dataSize=1)
print ("x5 = ", x5.__dict__)

x5.AddAditionalAtrib()
print ("After calling AddAditionalAtrib \nx5 = ", x5.__dict__)
