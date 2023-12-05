# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 07:21:50 2022

@author: msi1
"""

import matplotlib.pyplot as plt
import pandas as pd

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True,
                         sharey=True, figsize=(12,7))


x71 = pd.read_csv('stock_px.csv', parse_dates=True,
                  index_col=0)

x72 = x71[['AAPL', 'MSFT', 'XOM']]
x72 = x72.resample('B').ffill()

aapl_px = x72.AAPL['2005':'2009']

ma60 = aapl_px.rolling(window=30, min_periods=30).mean()
ewma60 = aapl_px.ewm(span=30, min_periods=0).mean()

aapl_px.plot(style='k-', ax=axes[0])
ma60.plot(style='k--', ax = axes[0])

aapl_px.plot(style='k-', ax=axes[1])
ewma60.plot(style='k--', ax=axes[1])

axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially weighted MA')

