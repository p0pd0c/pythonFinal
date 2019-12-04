class Card:
    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def show(self):
        print(f"Suit: {self.suit} | Value: {self.value}")

        