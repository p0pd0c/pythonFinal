from deck import Deck
from person import Person
from dealer import Dealer


def main():
    try:
        leaderboard = open('leaderboard.txt', 'r')
        leaders = {}
        wins = 0
        losses = 0
        print("_______________________________________________________________________________________________________")
        print("                                           Name/Win/Losses                                             ")
        for line in leaderboard:
            line = line.split(" ")
            print(line[0], "/", line[1], "/", line[2])
            leaders[line[0]] = [line[1], line[2]]
        leaderboard.close()
        print("_______________________________________________________________________________________________________")

        name = input("Give a name (used for leader board): ")
        while name == "" or not name.isalnum():
            name = input("Give a valid name (no spaces): ")

        print("*******************************************************************************************************")
        if name not in leaders:
            leaders[name] = [wins, losses]
            print(f"Hello {name}, you must be new around here. I will keep track of your scores for you")
        else:
            print(f"Welcome back {name}")
            wins = int(leaders[name][0])
            losses = int(leaders[name][1])

            if losses != 0:
                ratio = wins / losses
                print(f"Current W/L: {ratio}")
            elif wins == 0:
                print("Current W/L: 0")
            elif wins >= 1:
                print(f"Current W/L: {wins}")
        print("*******************************************************************************************************")
        play_again = True
        while play_again:
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
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
            if not player.is_bust(deck) and not dealer.is_bust(deck) and player.get_hand_total(
                    deck) >= dealer.get_hand_total(deck) or not player.is_bust(deck) and dealer.is_bust(deck):
                winner = player
                wins += 1
            else:
                winner = dealer
                losses += 1

            print("***************************************************************************************************")
            print("Winner:", winner.name)
            print("***************************************************************************************************")
            print("---------------------------------------------------------------------------------------------------")
            player.show()
            dealer.show()
            print("---------------------------------------------------------------------------------------------------")

            leaders[player.name][0] = wins
            leaders[player.name][1] = losses

            leaderboard = open("leaderboard.txt", 'w')
            for leader, stats in leaders.items():
                line = f"{leader} {stats[0]} {stats[1]}"
                leaderboard.write(line)
            leaderboard.close()

            play_again = input("Would you like to play again (Y/N): ")
            if play_again == 'Y':
                play_again = True
            else:
                play_again = False

    except Exception as err:
        print(err)
    finally:
        leaderboard.close()


main()
