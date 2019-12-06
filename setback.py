from deck import Deck
import random

# Ben Smith and Jared DiScipio, CS021
# a program that allows the user to play a card game called setback

# Setback Description:
# Setback is played with 4 players, with two teams trying to score more
# points than each other. Each game, players are each dealt 5 cards and
# then the first round starts with a round of betting in which
# players bet how many points they will get. Betting starts at 2 points, and
# can only go up to 4. The player who wins the betting round gets to play first
# and chooses the trump suite. Play then continues in the established playing
# order. In one round all four players will put down a card. The first person
# who plays a card decides the suit that the rest of the players will put down.
# Whoever puts down the highest card for that suit wins that round and takes
# all the cards from that round for their team. The play then begins next round
# with the winning player. The only exception to this rule
# is the trump suite. The trump suit is considered higher than any other card,
# even when the established suit is something else at the start of the round.
# So theoretically a 2 from the trump suit could beat an ace from the
# established suite for that round. By the end of each game, certain cards give
# the team points for the whole game. There are four points to be given out,
# The High, The Low, The Jack, and Points. to get the High, your team must
# possess the highest card played from the trump suit. Similarly, the low is
# the lowest played card from the trump suit and the Jack is the jack from the
# trump suit. the point for Points is determined by adding certain cards and
# whatever team has the higher number gets that point. The points that each
# team earned that game are then added onto their totals. However, if a team did
# not reach their bet, then that amount is subtracted from their score instead.
# Team scores can go into the negatives (for example, if a team had 5 points,
# bet 3 points the next round and didn't make that bet, then their score would
# be brought to 2). The team that did not bet is not affected by the bet and
# simply wins the points they get. the game ends when one of the teams reaches
# 11, but they must win on a round in which that team bet, so a team that gets
# to 11 on a round where they didn't bet does not win until they wina round they
# bet on.


# Card Values when adding up for points:
# Jack: 1
# Queen: 2
# King: 3
# Ace: 4
# 10: 10



# defines the main function. coded by Ben
def main():
    try:
        # takes in the users' names which will be used to tell them when it's their turn
        p1 = str(input("Player 1, please enter your name: "))
        p2 = str(input("Player 2, please enter your name (you will be on the same team as Player 1): "))
        p3 = str(input("Player 3, please enter your name: "))
        p4 = str(input("Player 4, please enter your name (you will be on the same team as Player 3): "))

        play(p1,p2,p3,p4)
        
    except ValueError:
        print("Your input was invalid.")

# defines a function to initiate the playing of the game. by Ben
def play(p1,p2,p3,p4):
    name1 = p1
    name2 = p2
    name3 = p3
    name4 = p4

    
    
# defines a program that will return a dictionary of 4 shuffled hands. by Ben
def getHands():

        hands = {}
    
    
        
# calls the main funtion
main()

