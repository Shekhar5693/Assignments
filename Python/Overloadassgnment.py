# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:42:50 2021

@author: shekh
"""

class Param:
    def __init__(self, n, v):
        self.n = n
        self.v = v
    
    def add(self):
        if isinstance(self.n,int):
            print("Sum is:", self.n + self.v)
        else:
            print("String is:", self.n + str(self.v))
    
    def mul(self):
        if isinstance(self.n,int):
            print("Product is:", self.n * self.v)
        else:
            print("String is:", self.n + str(self.v))
    
    def __str__(self):
         return "Print overload"
    
ob = Param("Don",2)
ob.add()
ob.mul()
print(ob)
