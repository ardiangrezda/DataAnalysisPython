# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 07:09:47 2022

@author: msi1
"""

import pandas as pd
df_macrodata = pd.read_csv('macrodata.csv')

print ("df_macrodata.head() = ", df_macrodata.head())

a = df_macrodata[['year','realgdp']]

a.plot()

a.realgdp.plot()
a.year.plot()

b = pd.read_csv('macrodata.csv',index_col='year')
c = b[['realgdp','realcons']]

c.loc[1960:1963].plot(kind='bar')
c.loc[1960:1963].plot(kind='barh')