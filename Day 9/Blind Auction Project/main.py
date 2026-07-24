import art
print(art.logo)

#create dictionary
bids = {}

repeat = True
while repeat == True:
    # TODO-1: Ask the user for input
    name = input("What is your name?")
    bid = int(input("What is your bid?"))   

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    more_bids = input("Any other bids? y/n")
    if more_bids == "n":
        repeat = False

    # TODO-4: Compare bids in dictionary
highest_bid = 0
name = ""
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        name = key

print(f"The winner is {name} with a bid of ${highest_bid}")





