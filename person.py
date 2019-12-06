class Person:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stay = False

    def action(self, deck, opponent):
        if not self.stay:
            self.show()
            print("Dealer's Hand: ")
            for card in opponent.hand[1:]:
                card.show()

            act = int(input("Hit Or Stay (0 | 1): "))
            if act == 0 and not self.is_bust(deck):
                self.hand.append(deck.deal())
                self.action(deck, opponent)
            else:
                self.stay = True

    def get_hand_total(self, deck):
        total = 0
        aces = 0
        for card in self.hand:
            if card.value in deck.royalCards and card.value != "Ace":
                total += 10
            elif card.value not in deck.royalCards:
                total += int(card.value)
            else:
                aces += 1
        for i in range(aces):
            if total + 11 <= 21:
                total += 11
            elif total + 11 > 21:
                total += 1

        return total

    def is_bust(self, deck):
        return self.get_hand_total(deck) > 21

    def show(self):
        print(f"{self.name}'s hand: ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for card in self.hand:
            card.show()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
