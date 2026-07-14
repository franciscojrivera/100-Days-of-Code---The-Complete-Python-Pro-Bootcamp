import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# the way I did it
random_integer = random.randint(0, 4)
print(friends[random_integer])

#2nd Option
print(random.choice(friends))
