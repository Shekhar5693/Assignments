# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:26:56 2021

@author: shekh
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def out_fun(a, b):
    def in_fun(a,b):
        return a + b
    return in_fun(a,b) + 5

print ("The sum of two number with increment of 5 is: ", out_fun(num1, num2))