# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:04:33 2021

@author: shekh
"""

print ("To buy battery based toys enter code 1.")
print ("To buy key based toys enter code 2.")
print ("To buy electrically chargeable toys enter code 3.")

code = int(input("Please enter a toy code: "))

amount = int(input("Please enter order amount in Rs: "))

# For battery based toys
if code == 1:
    print ("You are buying battery based toys.")
    
    if code == 1 and amount > 1000:
        print("You get 10% discount. Bill amount is Rs:  ", amount - (amount * 0.1))
    else:
        print ("Bill amount is Rs: ", amount)

# For key based toys
elif code == 2:
     print ("You are buying key based toys.")
     
     if code == 2 and amount > 100:
        print("You get 10% discount. Bill amount is Rs:  ", amount - (amount * 0.05))
     else:
        print ("Bill amount is Rs: ", amount)

# For electrically chargeable toys
elif code == 3:
     print ("You are buying electrically chargeable toys.")
     
     if code == 3 and amount > 500:
        print("You get 10% discount. Bill amount is Rs:  ", amount - (amount * 0.1))
     else:
        print ("Bill amount is Rs: ", amount)

else:
    print ("No entry found in product data base")