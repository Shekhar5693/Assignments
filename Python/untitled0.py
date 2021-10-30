# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:20:01 2021

@author: shekhar
"""

class BasicAccount():
    def __init__ (self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate
        
class MinimumAccount(BasicAccount):
    def __init__(self, name, minimum, penalty):
        self.minimum = 500
        self.penalty = 10
        