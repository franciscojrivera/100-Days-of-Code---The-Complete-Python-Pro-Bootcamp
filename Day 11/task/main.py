import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

#Ask player if they want to play
print("Do you want to play a game of Blackjack y/n")

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
hit = input("Would you like another card? y/n")


#TODO special case for Ace cards
while hit == "y":
    player.append(random.choice(cards))

    #Add score for player
    playerscore = sum(player)
    if playerscore > 21:
        print(f"Player: {player} score: {playerscore}")
        print(f"Dealer's first card: {dealer} score: {dealerscore}")
        print("You went over 21, you lose!")
        break

    print(f"Player: {player} score: {playerscore}")
    print(f"Dealer's first card: {dealer} score: {dealerscore}")
    hit = input("Would you like another card? y/n")

#player chooses to not deal anymore, dealers turn
while dealerscore < 17:
    dealer.append(random.choice(cards))
    dealerscore = sum(dealer)

#TODO if dealer goes over 21????

print(f"Player: {player} score: {playerscore}")
print(f"Dealer's first card: {dealer} score: {dealerscore}")

if playerscore > dealerscore:
    print("You win!")

elif playerscore == dealerscore:
    print("Draw")

else:
    print("You lose!")















