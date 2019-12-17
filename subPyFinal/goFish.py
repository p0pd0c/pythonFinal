# Ben Smith and Jared DiScipio, CS021
# a program that allows the user to play go fish with a computer player
import random


CARDS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
DECK = CARDS * 4


def go_fish():
    try:
        name = str(input("Please enter your name: "))  
    except ValueError:
        print("Your input was invalid.")

    play(name)

    
# runs through the game until cards have run out
def play(name):
    
    deck = DECK
    deck = list(deck)
    player = name
    playerScore = 0
    playerHand = []
    
    compScore = 0
    compHand = []
    # deals each player 8 cards
    for i in range(0,8):
        randChoice = random.choice(deck)
        playerHand.append(randChoice)
        deck.remove(randChoice)

        randChoice = random.choice(deck)
        compHand.append(randChoice)
        deck.remove(randChoice)
    turn = 0
    # loop continues until cards run out
    while (len(deck) > 0):
        # player plays first
        # this loop runs while the turn number is even
        # (while it is the player's turn)
        while (turn % 2 == 0):
            print("~~~~~~~~~~~~~~~~~~~")
            # prints the score
            print(name + ": " + str(playerScore) + " Computer: " + str(compScore))
            # prints the player's hand
            for i in range(len(playerHand)):
                print(playerHand[i], end = " ")

            # allows the player to guess a card that is in their hand
            guess = str(input("\nWhat card do you ask for? "))
            while guess not in playerHand:
                guess = str(input("You don't have that card. Choose another: "))
            print(name + " asks the computer for a " + guess + ".")

            # calls function that checks if the card is in the computer's hand
            guessGood = checkHand(guess,compHand)
            # if card isn't in computer's hand, end player turn and make them draw a new card
            if guessGood == False:
                print("Go Fish!")
                randChoice = random.choice(deck)
                playerHand.append(randChoice)
                deck.remove(randChoice)
                print(name + " drew a " + randChoice + " from the deck.")
                # if the player draws the card the asked the computer for, their turn continues.
                if randChoice != guess:
                    turn += 1
                else:
                    print("Lucky guess!")

            # else it takes the cards that match from the computer's hand
            else:
                for i in range(guessGood):
                    compHand.remove(guess)
                for i in range(guessGood):
                    playerHand.append(guess)
                if guessGood == 1:
                    print(name + " got " + str(guessGood) + " " + guess + " from the computer.")
                else:
                    print(name + " got " + str(guessGood) + " " + guess + "s from the computer.")

            # checks if the player has achieved a book (4 of the same cards)
            book = bookCheck(playerHand)
            # if they have, adds a point and removes cards from hand
            if book != False:
                print(name + " has achieved a book of " + book + "s!")
                playerScore += 1
                for i in range(4):
                    playerHand.remove(book)
                        # checks if either of the players' hands are empty, and lets them draw a new card
            if playerHand == [] and deck != []:
                print(name + "'s hand is empty. " + name + " takes a card from the deck.")
                randChoice = random.choice(deck)
                playerHand.append(randChoice)
                deck.remove(randChoice)
            if compHand == [] and deck != []:
                print("The computer's hand is empty. The computer takes a card from the deck.")
                randChoice = random.choice(deck)
                compHand.append(randChoice)
                deck.remove(randChoice)

            # checks if the deck is empty and breaks the loop if so
            if deck == []:
                break
        

        # loops while the turn number is odd (computer's turns)
        while (turn % 2 != 0):
            print("~~~~~~~~~~~~~~~~~~~")
            # prints the score
            print(name + ": " + str(playerScore) + " Computer: " + str(compScore))
            # prints the player's hand
            for i in range(len(playerHand)):
                print(playerHand[i], end = " ")

            guess = random.choice(compHand)

            print("\nThe computer asks " + name + " for a " + guess + ".")
            guessGood = checkHand(guess,playerHand)
            if guessGood == False:
                print("Go Fish!")
                randChoice = random.choice(deck)
                compHand.append(randChoice)
                deck.remove(randChoice)
                if randChoice != guess:
                    print("The computer drew a card from the deck.")
                    turn += 1
                else:
                    print("The computer drew a " + guess + " from the deck.")
                    print("Lucky guess!")
            else:
                for i in range(guessGood):
                    playerHand.remove(guess)
                for i in range(guessGood):
                    compHand.append(guess)
                if guessGood == 1:
                    print("The computer got " + str(guessGood) + " " + guess + " from " + name + ".")
                else:
                    print("The computer got " + str(guessGood) + " " + guess + "s from " + name + ".")
                            
            book = bookCheck(compHand)
            if book != False:
                print("The computer has achieved a book of " + book + "s!")
                compScore += 1
                for i in range(4):
                    compHand.remove(book)

            # checks if either of the players' hands are empty, and lets them draw a new card
            if playerHand == [] and deck != []:
                print(name + "'s hand is empty. " + name + " takes a card from the deck.")
                randChoice = random.choice(deck)
                playerHand.append(randChoice)
                deck.remove(randChoice)
            if compHand == [] and deck != []:
                print("The computer's hand is empty. The computer takes a card from the deck.")
                randChoice = random.choice(deck)
                compHand.append(randChoice)
                deck.remove(randChoice)

            # checks if the deck is empty and breaks the loop if so
            if deck == []:
                break


    print("The deck is empty!")
    # after the loop completes, the game is almost over. whoever has more points after all cards are down wins
    while playerHand != [] and compHand != []:
        # turn syestem remains the same as before
        while (turn % 2 == 0):
            print("~~~~~~~~~~~~~~~~~~~")
            # prints the score
            print(name + ": " + str(playerScore) + " Computer: " + str(compScore))
            # prints the player's hand
            for i in range(len(playerHand)):
                print(playerHand[i], end = " ")

            # allows the player to guess a card that is in their hand
            guess = str(input("\nWhat card do you ask for? "))
            while guess not in playerHand:
                guess = str(input("You don't have that card. Choose another: "))
            print(name + " asks the computer for a " + guess + ".")

            # calls function that checks if the card is in the computer's hand
            guessGood = checkHand(guess,compHand)
            # if card isn't in computer's hand, end player turn and make them draw a new card
            if guessGood == False:
                print("Go Fish!")
                print("No cards left in the deck.")
                turn += 1
                # if the player draws the card the asked the computer for, their turn continues.

            # else it takes the cards that match from the computer's hand
            else:
                for i in range(guessGood):
                    compHand.remove(guess)
                for i in range(guessGood):
                    playerHand.append(guess)
                if guessGood == 1:
                    print(name + " got " + str(guessGood) + " " + guess + " from the computer.")
                else:
                    print(name + " got " + str(guessGood) + " " + guess + "s from the computer.")

            # checks if the player has achieved a book (4 of the same cards)
            book = bookCheck(playerHand)
            # if they have, adds a point and removes cards from hand
            if book != False:
                print(name + " has achieved a book of " + book + "s!")
                playerScore += 1
                for i in range(4):
                    playerHand.remove(book)

            # checks if the scores have been maxed out
            if compScore + playerScore == 13:
                break
        # loops while the turn number is odd (computer's turns)
        while (turn % 2 != 0):
            print("~~~~~~~~~~~~~~~~~~~")
            # prints the score
            print(name + ": " + str(playerScore) + " Computer: " + str(compScore))
            # prints the player's hand
            for i in range(len(playerHand)):
                print(playerHand[i], end = " ")

            guess = random.choice(compHand)

            print("\nThe computer asks " + name + " for a " + guess + ".")
            guessGood = checkHand(guess,playerHand)
            if guessGood == False:
                print("Go Fish!")
                print("No cards left in the deck.")
                turn += 1
            else:
                for i in range(guessGood):
                    playerHand.remove(guess)
                for i in range(guessGood):
                    compHand.append(guess)
                if guessGood == 1:
                    print("The computer got " + str(guessGood) + " " + guess + " from " + name + ".")
                else:
                    print("The computer got " + str(guessGood) + " " + guess + "s from " + name + ".")
                
            book = bookCheck(compHand)
            if book != False:
                print("The computer has achieved a book of " + book + "s!")
                compScore += 1
                for i in range(4):
                    compHand.remove(book)
            # checks if the scores have been maxed out
            if compScore + playerScore == 13:
                break

    # determines the winner
    # prints the score
    print(name + ": " + str(playerScore) + " Computer: " + str(compScore))
    if playerScore > compScore:
        print(name + ' wins! Your victory has been recorded in "goFishScores.txt"!')
    else:
        print('The computer wins! Better luck next time! The results of your game have been recorded in "goFishScores.txt".')
    record(name,playerScore,compScore)
                

# function to test bookCheck()
def bookTest():
    tst = [7,6,8,7,7,8,7,2]
    test = [4,5,6]
    tes = [4,5,6,7,8,9,10]
    print(bookCheck(tst))
    print(bookCheck(test))
    print(bookCheck(tes))

# checks if the hand in question has a book. if it does, returns that card's
# value, else returns false.
def bookCheck(hand):
    if len(hand) < 4:
        return False
    else:
        for i in hand:
            count = 0
            check = [] + hand
            for j in check:
                if j == i:
                    count += 1
            if count == 4:
                return i
        return False

# a function that checks to see how many times a value appears in a hand and
# returns how many times it shows up in the hand
def checkHand(val,hand):
    counter = 0
    for i in hand:
        if val == i:
            counter += 1
    if counter > 0:
        return counter
    else:
        return False
    
# a function that records the player's game information to a file called goFishScores.txt
def record(name,pScore,cScore):
    infile = open("goFishScores.txt", "a")
    if pScore > cScore:
        infile.write(name + " lost to the computer with a score of " + str(pScore) + " to " + str(cScore) + "\n")
    else:
        infile.write(name + " beat the computer with a score of " + str(pScore) + " to " + str(cScore) + "!\n")


