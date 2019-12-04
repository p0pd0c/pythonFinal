import random
from card import Card


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
            print(e)

