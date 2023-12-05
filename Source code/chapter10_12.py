# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 07:00:45 2022

@author: msi1
"""

import pandas as pd
df_macrodata = pd.read_csv('macrodata.csv')

print ("df_macrodata.head() = \n ", df_macrodata.head())

a = df_macrodata[['year','realgdp']]

a.plot()
a.realgdp.plot()

b = pd.read_csv('macrodata.csv', index_col='year')

c = b[['realgdp','realcons']]

c.loc[1960:1963].plot(kind='bar')
c.loc[1960:1963].plot(kind='barh')
