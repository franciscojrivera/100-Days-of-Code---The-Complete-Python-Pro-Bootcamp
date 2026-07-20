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