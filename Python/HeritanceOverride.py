# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:24:37 2021

@author: shekh
"""

class Address:
    def __init__ (self, street, num):
        self.street_name = street
        self.number = num

class CampusAddress(Address):
    def __init__ (self, office_number, num = 77, street = "Massachusetts Ave"):
        #Address.__init__(self, street,num)
        self.street_name = street
        self.number = num
        self.office_number = office_number
        
Sarina_addr = CampusAddress("32-G904")
print(Sarina_addr.office_number)
print(Sarina_addr.street_name)
print(Sarina_addr.number)
