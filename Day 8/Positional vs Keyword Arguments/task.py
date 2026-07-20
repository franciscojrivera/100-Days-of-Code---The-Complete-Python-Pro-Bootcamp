# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with_name(name, location):
    print(f"Hello, {name}! You are at {location}")

greet_with_name("Francisco", "Los Angeles")
greet_with_name(location="Los Angeles", name="Francisco")

#Love Calculator
def calculate_love_score(name1 , name2):
    true = ['t', 'r', 'u', 'e']
    love = ['l', 'o', 'v', 'e']

    true_count = 0
    love_count = 0

# Check true count for both names
    for char in name1:
        for char2 in true:
            if char == char2:
                true_count += 1

    for char in name2:
        for char2 in true:
            if char == char2:
                true_count += 1

#Check love count for both names
    for char in name1:
        for char2 in love:
            if char == char2:
                love_count += 1

    for char in name2:
        for char2 in love:
            if char == char2:
                love_count += 1

    total = str(true_count) + str(love_count)
    print(total)

calculate_love_score("Francisco Rivera", "Carolyn Kim")
