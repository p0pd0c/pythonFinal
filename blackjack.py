from deck import Deck
from person import Person
from dealer import Dealer


def main():
    play_again = True

    name = input("Give a name (used for leader board): ")
    while name == "":
        name = input("Give a valid name (used for leader board): ")

    while play_again:
        player = Person(name)

        dealer = Dealer("BlackJack Expert 123")

        deck = Deck()
        deck.build()
        deck.shuffle()

        player.hand = [deck.deal(), deck.deal()]

        dealer.hand = [deck.deal(), deck.deal()]

        player.action(deck, dealer)

        dealer.action(deck, player)

        winner = None
        if not player.is_bust(deck) and not dealer.is_bust(deck) and player.get_hand_total(deck) >= dealer.get_hand_total(deck) or not player.is_bust(deck) and dealer.is_bust(deck):
            winner = player
        else:
            winner = dealer

        print("Winner:", winner.name)
        player.show()
        dealer.show()

        play_again = input("Would you like to play again (Y/N): ")
        if play_again == 'Y':
            play_again = True
        else:
            play_again = False


main()
