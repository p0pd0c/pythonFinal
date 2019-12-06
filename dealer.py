# Jared DiScipio | CS021 Gold | Final | Blackjack

from person import Person


# Inherits a lot of functionality from Person class
# Plays all on its own, following a simple blackjack rule set
class Dealer(Person):
    def __init__(self, name):
        # Call constructor of Person with the provided name because Dealer inherits from Person
        super().__init__(name)

    # Recursively hit or stay depending on current hand and status of opponent
    def action(self, deck, opponent):
        if not self.stay:
            if not self.is_bust(deck) and self.get_hand_total(deck) < 17 and not opponent.is_bust(deck):
                self.hand.append(deck.deal())
                # Enter back into function to decide again
                self.action(deck, opponent)
            else:
                self.stay = True
