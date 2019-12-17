# Ben Smith and Jared DiScipio

import goFish
import blackjack


# This is the swap between go fish and blackjack
# Ben Smith, Jared DiScipio
def main():
    play_again = True
    while play_again:
        print("0) Blackjack")
        print("1) Go Fish")

        choice = input("Choice: ")
        while not choice.isnumeric():
            choice = input("Choice: ")

        choice = int(choice)
        if choice == 0:
            blackjack.blackjack()
        else:
            goFish.go_fish()

        play_again = input("Would you like to play again (Y/N): ")
        if play_again != "Y":
            play_again = False


main()
