# Jared DiScipio | CS021 Gold | Final | Blackjack

# A person object for blackjack
# Needs a name upon creation
# Keeps track of own hand and game status
class Person:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stay = False

    # Recursively allow the player to continue playing  until they bust => stay or stay
    def action(self, deck, opponent):
        if not self.stay:
            self.show()
            print("Dealer's Hand: ")
            for card in opponent.hand[1:]:
                card.show()

            act = int(input("Hit Or Stay (0 | 1): "))
            if act == 0 and not self.is_bust(deck):
                self.hand.append(deck.deal())
                # Enter back into function to ask for next play
                self.action(deck, opponent)
            else:
                self.stay = True

    # Add up the value of the hand
    def get_hand_total(self, deck):
        total = 0
        aces = 0
        for card in self.hand:
            # Add up all non aces, face cards worth 10
            if card.value in deck.royalCards and card.value != "Ace":
                total += 10
            elif card.value not in deck.royalCards:
                total += int(card.value)
            else:
                aces += 1

        # Now account for all aces, making sure that they are added as either 1 or 11 depending on current total
        for i in range(aces):
            if total + 11 <= 21:
                total += 11
            elif total + 11 > 21:
                total += 1

        return total

    # Tell whether or not person has exceeded 21
    def is_bust(self, deck):
        return self.get_hand_total(deck) > 21

    # Display the current hand
    def show(self):
        print(f"{self.name}'s hand: ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for card in self.hand:
            card.show()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
