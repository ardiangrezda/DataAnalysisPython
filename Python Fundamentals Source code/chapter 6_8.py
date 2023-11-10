# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 07:17:06 2021

@author: msi1
"""

class rectangle():
    def __init__(self, l = 1, w = 2):
        self.length = l
        self.width = w
    @property
    def Length(self):
        return self.length
    @Length.setter
    def Length(self, value):
        self.length = value
    @property
    def Width(self):
        return self.width
    @Width.setter
    def Width(self, value):
        self.width = value
    def Perimeter(self):
        p = 2 * self.width + 2 * self.length
        return p
    def Area(self):
        a = self.width * self.length
        return a
    def IsSquare(self):
        if self.width == self.length:
            print ("This is square")
        else:
            print ("this is rectangle")
            
a = rectangle(5, 2)
print ("Perimeter of a = ", a.Perimeter())

b = rectangle(7, 9)
print ("Area of b = ", b.Area())

c = rectangle(5,5)
c.IsSquare()

class Dog():
    def __init__(self, n, t):
        self.name = n
        self.trick = t
    def add_trick(self, t):
        self.trick.append(t)
        
d = Dog("Bubi", ["Play", "Sleep", "Walk", "Run"])
e = Dog("Fido", ["Bend"])
print ("d = ", d.__dict__)
print ("e = ", e.__dict__)
e.add_trick("Walk")
print ("After add_trick, e = ", e.__dict__)


class Customer():
    def __init__(self, n, b):
        self.name = n
        self.balance = b
    def Withdraw(self, value):
        if self.balance > value:
            self.balance = self.balance - value
        else:
            print ("You cannot withdraw")
    def Deposit(self, value):
        self.balance += value
        
f = Customer("Ardian", 1000)
f.Withdraw(1100)
f.Deposit(10000)
print ("After deposit: ", f.__dict__)
f.Withdraw(100)
print ("After withdraw: ", f.__dict__)
    
