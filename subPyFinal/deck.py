# Jared DiScipio | CS021 Gold | Final | Blackjack

import random
from card import Card


# Keeps track of cards
# Can be made empty
# Can be 'built' to have a sorted deck
# Can be shuffled to make it a shuffled deck
# Can be displayed
# Cards can be dealt and they will leave the deck
class Deck:
    def __init__(self):
        self.values = []
        self.royalCards = ["Jack", "Queen", "King", "Ace"]
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.cards = []

        for i in range(2, 11):
            self.values.append(str(i))

        self.values += self.royalCards

    def build(self):
        for s in self.suits:
            for v in self.values:
                self.cards.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        for card in self.cards:
            card.show()

    def deal(self):
        try:
            return self.cards.pop()
        except IndexError as e:
            print("The deck is empty")

