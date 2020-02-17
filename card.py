# Author : Georgia Mandell
# Date : 02/07/2020
# Purpose : write a Card class


class Card:

    def __init__(self, num, suit):

        # assigning string values to variables for card values based on integer values of parameters
        if 1 < num <= 10:
            self.num = str(num)
        elif num == 1:
            self.num = "Ace"
        elif num == 11:
            self.num = "Jack"
        elif num == 12:
            self.num = "Queen"
        elif num == 13:
            self.num = "King"

        # assigning string values to variables for suits based on integer values of parameters
        if suit == 1:
            self.suit = "clubs"
        elif suit == 2:
            self.suit = "spades"
        elif suit == 3:
            self.suit = "diamonds"
        elif suit == 4:
            self.suit = "hearts"

    def __str__(self):
        return(self.num + " of " + self.suit)



