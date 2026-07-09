print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip / 100)

tip = bill * tip

total = bill + tip

total = round(total, 2)

print(f"The total bill is: ${total}")

total = total / people

print(f"Each person should pay: ${round(total, 2)}")

