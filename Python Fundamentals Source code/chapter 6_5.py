# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 07:34:07 2021

@author: msi1
"""
class DataVis(object):
    def __init__(self, data=None, dataSize=0):
        self.data = data
        self.dataSize = dataSize
    def MethodNotImplemented(self):
        raise NotImplementedError("This has not been implemented")
        
a = DataVis()
a.MethodNotImplemented()

