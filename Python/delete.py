# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:23:17 2021

@author: shekh
"""

from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "(%s,%s)" %(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        for i in self.cards:
            print(i)

    def __repr__(self):
        return "Cards remaining in deck: {}".format(len(self.cards))
   
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
            return self.cards
        else:
            return("Only full decks can be shuffled")

    def deal(self):
        if len(self.cards) != 0:
            return self.cards.pop()
        else:
            return("All cards have been dealt")

d=Deck()
print("Deck created")

print("\n \n Shuffling the deck")
x=d.shuffle()
for i in x:
    print(i)
a=int(input("\n \n Enter 1 to deal the cards \n"))

while(a==1):
    print(d.deal())
    print(d)
    a=int(input("Enter 1 to deal the cards (or) any key to discontinue \n"))
print(d.shuffle())