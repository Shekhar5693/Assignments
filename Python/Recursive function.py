# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:08:50 2021

@author: shekh
"""

a = int(input("Please enter a number: "))

def recursive(a):
    if a == 1:
        return a
    else:
        return a + recursive(a - 1)

print("The sum is: ", recursive(a))