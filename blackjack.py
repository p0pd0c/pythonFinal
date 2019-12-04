from deck import Deck


def main():
    my_deck = Deck()
    my_deck.build()
    my_deck.shuffle()
    # my_deck.show()

    busted = False

    player_cards = [my_deck.deal(), my_deck.deal()]
    dealer_cards = [my_deck.deal(), my_deck.deal()]


main()
