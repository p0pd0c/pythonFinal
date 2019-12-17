# Jared DiScipio | CS021 Gold | Final | Blackjack


# Holds a suit and a value
# Can be shown
class Card:
    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def show(self):
        print(f"{self.value} of {self.suit}")
