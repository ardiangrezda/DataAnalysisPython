# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 07:02:24 2021

@author: msi1
"""

# task 2
ex = 'Both of these genres made a big impact on cinematic storytelling'

a2 = ex[:4]
a3 = ex[0]
a4 = ex[-12:]
a5 = ex[::-1]

print ("a2 = ", a2)
print ("a3 = ", a3)
print ("a4 = ", a4)
print ("a5 = ", a5)

print ("-----------------------------------")

# task 3
ls = [4, 3.1415, 1.0, 'Hello', 'World']
print ("ls = ", ls)
#ls.pop(2)
ls.remove(1.0)
print ("After remove, ls = ", ls)
ls.append(31)
print ("After append, ls = ", ls)
ls.extend([2.0, 34, 'Mars'])
print ("After extend, ls = ", ls)


print ("-----------------------------------")

#task 4
x = {'alpha': 1.0, 'beta':3.1415, 'gamma': 99}
print ("x = ", x)
print ("x['alpha'] = ", x['alpha'])