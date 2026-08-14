import art
import random
import sys

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

blackjack = input("Do you want to play a game of Blackjack y/n ")

#Ask player if they want to play
while blackjack == 'y':

    #Deal two cards for player
    player.append(random.choice(cards))
    player.append(random.choice(cards))

    #Add score for player
    playerscore = sum(player)

    print(f"Player: {player} score: {playerscore}")

    #Deal one card for dealer
    dealer.append(random.choice(cards))

    dealerscore = sum(dealer)

    print(f"Dealer's first card: {dealer[0]}")

    #Ask player if they want another card
    hit = input("Would you like another card? y/n ")



    while hit == "y":
        player.append(random.choice(cards))
        #Add score for player
        playerscore = sum(player)

        #if player is over 21 but contains 11, turn 11 card into a 1
        if playerscore > 21 and 11 in player:
            #iterate through list and turn 11s into 1s, keeping same list
            for index, value in enumerate(player):
                if value == 11:
                    player[index] = 1

        #update sum since value was changed
        playerscore = sum(player)

        #TODO fix this line of code
        if playerscore > 21:
            break



        print(f"Player: {player} score: {playerscore}")
        print(f"Dealer's first card: {dealer} score: {dealerscore}")
        hit = input("Would you like another card? y/n")

    #player chooses to not deal anymore, dealers turn
    while dealerscore < 17:
        dealer.append(random.choice(cards))
        dealerscore = sum(dealer)

    #if player is over 21 but contains 11, turn 11 card into a 1
    if dealerscore > 21 and 11 in dealer:
    #iterate through list and turn 11s into 1s, keeping same list
        for index, value in enumerate(dealer):
            if value == 11:
                dealer[index] = 1

    #update sum since value was changed
    dealerscore = sum(dealer)


    print(f"Player: {player} score: {playerscore}")
    print(f"Dealer: {dealer} score: {dealerscore}")

    if dealerscore > 21:
        print("You win!")

    elif playerscore > dealerscore:
        print("You win!")

    elif playerscore == dealerscore:
        print("Draw")

    else:
        print("You lose!")

    blackjack = input("Do you want to play a game of Blackjack y/n")

    #reset deck of cards
    player = []
    dealer = []















