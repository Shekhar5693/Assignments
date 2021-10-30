# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:54:47 2021

@author: shekh
"""
print ("To buy battery based toys enter code 1.")
print ("To buy key based toys enter code 2.")
print ("To buy electrically chargeable toys enter code 3.")

code = int(input("Enter the toy code: "))
amount = int(input("Please enter order amount in Rs: "))

def discount():
    if code == 1:
        if amount > 1000:
            a = amount * 0.1
        else:
            a = 0
    
    elif code == 2:
        if amount > 100:
            a = amount * 0.05
        else:
            a = 0
    
    elif code == 3:
        if amount > 500:
            a = amount * 0.1
        else:
            a = 0
    
    else:
        print ("No entry found in product data base")
    return a
    
net_amount= amount - discount()
print ("Bill amount is Rs: ", net_amount)
