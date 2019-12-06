from person import Person


class Dealer(Person):
    def __init__(self, name):
        super().__init__(name)

    def action(self, deck, opponent):
        if not self.stay:
            if not self.is_bust(deck) and self.get_hand_total(deck) < 17 and not opponent.is_bust(deck):
                self.hand.append(deck.deal())
                self.action(deck, opponent)
            else:
                self.stay = True
