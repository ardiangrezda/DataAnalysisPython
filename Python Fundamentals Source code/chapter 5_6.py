# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:52:31 2021

@author: msi1
"""

def Func8(x, y, p=2):
    """ The docstring can be used for help about the function.
    A good docstring should explain the input parameters and 
    return value and what a function's purpose
    """
    d = x - y
    return sum(abs(d)**p)
