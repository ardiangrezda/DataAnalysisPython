# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 08:32:03 2022

@author: msi1
"""

import pandas as pd

x71 = pd.read_csv('stock_px.csv', parse_dates=True,
                  index_col=0)
print ("x71 = \n", x71)
print ("-----------------------------------")

x72 = x71[['AAPL', 'MSFT', 'XOM']]
x72 = x72.resample('B').ffill()

print ("x72 = \n", x72)
print ("-----------------------------------")

x72['AAPL'].plot()

x72.loc['2009'].plot()