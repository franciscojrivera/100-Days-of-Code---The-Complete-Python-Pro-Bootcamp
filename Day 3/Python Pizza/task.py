print("Welcome to Python Pizza Deliveries!")
bill = 0
pizza = ""
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    pizza = size
    bill += 15
elif size == "M":
    pizza = size
    bill += 20
elif size == "L":
    pizza = size
    bill += 25
else:
    print("Sorry, please enter S, M, or L")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if pizza == "S":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")

