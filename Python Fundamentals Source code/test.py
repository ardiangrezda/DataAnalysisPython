# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 06:39:04 2021

@author: msi1
"""

def square(x):
    return x * x

if __name__ == "__main__":
    print ("Program called directly")
else:
    print ("Program called indirectly using name", __name__)
