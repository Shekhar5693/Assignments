# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:58:34 2021

@author: shekh
"""
file = open("Bank.txt", "a")

class BasicAccount():
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.myRate = 0
        self.cd = 0
               
    def name(self):
        return self.name
    
    def mybalance(self):
        return self.balance
    
    def rate(self):
        file.write("\nInterest on your current balance is:" + str(self.myRate))
        return self.myRate
        
    
    def deposit(self, amount):
            self.balance += amount
            
    def withdraw(self, amount):
        if amount > self.balance:
                print("Insufficient Balance. Available balance is: ", self.balance)
                file.write("\nInsufficient Balance. Available balance is: " + str(self.balance))
        else:
            self.balance -= amount
            
    def interest(self,rate):
        month = rate / 12
        self.myRate = self.balance * month
        
    def cdCreate(self, amount):
        self.cd = amount
        
    def cdReturn(self, months, rate):
        amount = self.cd * (pow((1 + rate / 100), months))
        ci = amount - self.cd
        print("Returns at the end of term:",amount)
        file.write("\nReturns at the end of term:" + str(amount))
        print("You will get interest of:", ci)
        file.write("\nYou will get interest of:" + str(ci))
        
class ProtectedAccount(BasicAccount):
    def __init__(self, name, pin):
        self.pin = None
        super().__init__(name)
        self.pin = pin
        
        
    def depositPinCheck(self,pin, amount):
        if self.pin == pin:
            self.deposit(amount)
        else:
            file.write("\nIncorrect PIN)")
            raise Exception ("Incorrect PIN")            
            
    def withdrawPinCheck(self, pin, amount):
        if self.pin == pin:
            self.withdraw(amount)
        else:
            file.write("\nIncorrect PIN)")
            raise Exception ("Incorrect PIN")            
            
    def interestPinCheck(self, pin, rate):
        if self.pin == pin:
            self.interest(rate)
        else:
            file.write("\nIncorrect PIN)")
            raise Exception ("Incorrect PIN")           
            
    def cdPinCheck (self, pin, amount):
        if self.pin == pin:
            self.cdCreate(amount)
        else:
            file.write("\nIncorrect PIN)")
            raise Exception ("Incorrect PIN")

class MinimumAccount(ProtectedAccount):
    def __init__(self, name, pin, minimum, penalty, ):
        self.minimum = 0
        self.penalty = 0
        self.chargePenalty = False
        
        super().__init__(name, pin)
        self.minimum = minimum
        self.penalty = penalty
        self.chargePenalty = False
        
    def withdraw1(self, pin, amount):
        self.withdrawPinCheck(pin, amount)
        if self.balance < self.minimum:
            self.chargePenalty = True
        else:
            pass
    
    def __repr__(self):
        print("Balance is:", self.mybalance())
        file.write("\nBalance is:" + str(self.balance))

class InterestAccount(ProtectedAccount):
    def __init__(self, name, pin):
        super().__init__(name, pin)
        
    def depositMoney(self, pin, amount):    
        self.depositPinCheck(pin, amount)
    
    def myInterest(self,pin, rate):
       self.interestPinCheck(pin, rate)

class CDAccount(ProtectedAccount):
    def __init__(self, name, pin ):
        super().__init__(name, pin)
    
    def createCD(self,pin, amount):
        self.cdPinCheck (pin, amount)
    
    def checkCDReturn(self, months, rate):
        self.cdReturn(months, rate)

class RegularAccount(MinimumAccount):
    def __init__(self, name, pin, balance):
        super().__init__(name, pin, minimum = 500, penalty = 10)
        self.balance = balance
        
    def depositMoney(self, pin, amount):    
        self.depositPinCheck(pin, amount)
        
    def withdrawMoney(self, pin, amount):
        super().withdraw1(pin, amount)
        if self.chargePenalty == True:
            print("Penalty of 10 will be deducted from your account next month for not maintaining minimum amount of 500")
            file.write("Penalty of 10 will be deducted from your account next month for not maintaining minimum amount of 500")
           
class CheckingAccount(MinimumAccount):
    def __init__(self, name, pin):
        super().__init__(name, pin, minimum = 500, penalty = 10)
    
    def depositMoney(self, pin, amount):    
        self.depositPinCheck(pin, amount)
        
    def balanceCheck(self):
        super().__repr__()
    
    def nameCheck(self):
        print("Name of account holder is:", self.name)
        file.write("\nName of account holder is: " + self.name)
    
    def minimumCheck(self):
        print("Minimum account balance to be maintained:",self.minimum)
        file.write("\nMinimum account balance to be maintained: " + str(self.minimum))
    
    def penaltyCheck(self):
        print("Penalty if failed to maintain minimum balance:",self.penalty)
        file.write("\nPenalty if failed to maintain minimum balance: " + str(self.penalty))
 
file.write("Welcome to NO Bank")       
file.write("\n\nPlease select: \n1 for deposit. \n2 for withdrawal \n3 for creating CD account \n4 for checking interest \n5 for checking account details\n")
a = int(input("Please select: \n1 for deposit. \n2 for withdrawal \n3 for creating CD account \n4 for checking interest \n5 for checking account details\n"))        
file.write("\n"+str(a))
 
if a == 1:
    file.write("\nDeposit:")
    obj = RegularAccount("Sam", 1234, 500)
    b = int(input("Please enter your pin:")) 
    file.write("\nPlease enter your pin:")
    c= int(input("Please enter amount:"))
    file.write("\nEnter ammount:")
    file.write("\n" + str(c))
    obj.depositMoney(b,c)
    print("Amount credited to your account. Your current balance is:$", obj.balance)
    file.write("\nAmount credited from your account. Your current balance is:" + str(obj.balance))

elif a == 2:
    file.write("\nWithdraw:")
    obj = RegularAccount("Sam", 1234, 600)
    b = int(input("Please enter yout PIN:"))
    file.write("\nPlease enter your pin:")
    c= int(input("Please enter amount:"))
    file.write("\nPlease enter amount:")
    file.write("\n" + str(c))
    obj.withdrawMoney(b,c)
    print("Amount debited from your account. Your current balance is:$", obj.balance)
    file.write("\nAmount debited from your account. Your current balance is:" + str(obj.balance))

elif a == 3:
    file.write("\nCD Account:")
    obj = CDAccount("Sam", 1234)
    b = int(input("Please enter yout PIN:"))
    file.write("\nPlease enter your pin:")
    c= int(input("Please enter amount:"))
    file.write("\nPlease enter amount:")
    file.write("\n" + str(c))
    obj.cdPinCheck(b,c)
    print("Your CD account has been created with:$", obj.cd)
    file.write("\nYour CD account has been created with:" + str(obj.cd))
    d = input("Do you want to check returns on your CD account at end of term? \nEnter 'y' for yes or 'n' for no:")
    file.write("\nDo you want to check returns on your CD account at end of term? \nEnter 'y' for yes or 'n' for no:")
    file.write("\n" + d)
    if d == "y":
        obj.checkCDReturn(12, 10)
    elif d == "n":
        pass
 
elif a == 4:
    file.write("\nInterest on balance:")
    obj = InterestAccount("Sam", 1234)
    obj.deposit(1234)
    b = int(input("Please enter your pin:")) 
    file.write("\nPlease enter your pin:")
    obj.myInterest(b, 2.55)
    print("Interest on your current balance is:",obj.rate())

elif a==5:
    file.write("\nDetails")
    obj = CheckingAccount("Sam", 1234)
    obj.depositMoney(1234, 500)
    obj.balanceCheck()
    obj.nameCheck()
    obj.minimumCheck()
    obj.penaltyCheck()
    
else:
    print("Please enter valid number")
    file.write("Please enter valid number")
    
file.close()
    
    
            
        
    