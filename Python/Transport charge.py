# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:45:53 2021

@author: shekh
"""

km = int(input("Please enter the distance in kilometers to calculate fare: "))

if km in range(1,50):
    print("The fare is: ", km * 8)
elif km in range(51,100):
    print("The fare is: ", km * 10)
elif km > 100:
    print("The fare is: ", km * 12)
else:
    print("Please enter a valid number")