# Author : Georgia Mandell
# Date : 02/07/2020
# Purpose : write a Deck class

import random
from card import Card


class Deck:

    def __init__(self):
        # list that holds cards in deck
        self.card_list = []

    def add_standard_cards(self):
        self.num = 1
        self.suit = 1

        # adding 52 cards to card list: one for each value, for each suit
        while self.suit <= 4:
            self.num = 1
            while self.num <= 13:

                self.newcard = Card(self.num, self.suit)
                self.add(self.newcard)
                self.num = self.num + 1

            self.suit = self.suit + 1

    # looping through self.card list and swapping each item into a random location
    def shuffle(self):

        for i in range(len(self.card_list)-1):
            new_loc = random.randint(0, len(self.card_list) - 1) # generating random number for new location of current card
            temp = self.card_list[new_loc] # creating a temporary variable to store the card in the new location
            self.card_list[new_loc] = self.card_list[i] # storing the card at current location i in the new location new_loc
            self.card_list[i] = temp # storing temporary variable in current location

    # adds new card to card list
    def add(self, card):
        self.card_list.append(card)

    # removes the last five cards from card list and stores in a new list
    def deal(self,num):
        # creating new tiny deck to represent a hand
        hand = Deck()

        # adds last five cards from card list to hand and removes those cards from card list
        for i in range(num):
            # pop() removes the last item from a list and returns the value of that item
            card = self.card_list.pop()
            hand.add(card)

        return hand

